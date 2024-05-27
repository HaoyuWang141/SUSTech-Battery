from enum import Enum
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Stage(Enum):
    CC_IN = 0
    CV_IN = 1
    IDLE_IN = 2
    CC_OUT = 3
    IDLE_OUT = 4


def read_data(capacity_file, curve_file):
    df_capacity = pd.read_excel(capacity_file)
    df_curve = pd.read_excel(curve_file)

    def map_stage_to_enum(stage, last_stage):
        if stage == "恒流充电":
            return Stage.CC_IN
        elif stage == "恒压充电":
            return Stage.CV_IN
        elif stage == "搁置" and (
            last_stage == Stage.CV_IN or last_stage == Stage.IDLE_IN
        ):
            return Stage.IDLE_IN
        elif stage == "恒流放电":
            return Stage.CC_OUT
        elif stage == "搁置" and (
            last_stage == Stage.CC_OUT or last_stage == Stage.IDLE_OUT
        ):
            return Stage.IDLE_OUT
        else:
            raise ValueError("Unknown stage")

    CURVES = []

    # curve in CURVES:
    """
    curve = {
        data: [[voltage, current], [voltage, current], ...],
        stages: [(idx, idx), (idx, idx), ...], # idx is the index of stage, [idx, idx]
    }
    """

    stage, last_stage = None, None
    idx_start, idx_end = 0, -1
    cycle_num, last_cycle_num = 1, None
    data_list = []
    stages = []

    for i, row in df_curve.iterrows():
        idx_end += 1
        data = row[["电流(A)", "电压(V)"]].values.tolist()
        stage = map_stage_to_enum(row["工步类型"], last_stage)
        if last_stage is None:
            last_stage = stage
        if stage == last_stage:
            data_list.append(data)
            continue

        last_stage = stage
        stages.append((idx_start, idx_end))

        cycle_num = row["循环号"]
        if last_cycle_num is None:
            last_cycle_num = cycle_num

        if cycle_num == last_cycle_num:
            idx_start = idx_end
            data_list.append(data)
            continue

        curve = {
            "data": data_list,
            "stages": stages,
        }
        CURVES.append(curve)
        data_list = [data]
        stages = []
        idx_start, idx_end = 0, 0
        last_cycle_num = cycle_num

    LABELS = df_capacity["放电容量(Ah)"].values
    if len(LABELS) != len(CURVES):
        num_data = min(len(LABELS), len(CURVES))
        LABELS = LABELS[:num_data]
        CURVES = CURVES[:num_data]

    print(f"Total {len(CURVES)} curves, Total {len(LABELS)} labels")
    print(
        f"The first curve has {len(CURVES[0]['data'])} data points and {len(CURVES[0]['stages'])} stages"
    )

    return CURVES, LABELS


def get_closest_idx(arr, target):
    return np.argmin(np.abs(arr - target))


def get_training_data(curves, labels, num_v, num_i):
    """
    将数据转换为训练数据，截取相同长度的电压和电流数据
    电压数据来源于恒压充电阶段的末尾，电流数据来源于恒流放电阶段的开头
    """
    valid_labels = []
    voltage_CC = []
    current_CV = []
    for index, curve in enumerate(curves):
        if len(curve["stages"]) < 5:
            print(f"第{index+1}组数据不完整，跳过；它的stages是：")
            print(curve["stages"])
            continue
        
        CC = curve["stages"][Stage.CC_IN.value]
        CV = curve["stages"][Stage.CV_IN.value]
        data_CC = curve["data"][CC[0] : CC[1]]
        data_CV = curve["data"][CV[0] : CV[1]]
        v_CC = [d[1] for d in data_CC]
        i_CV = [d[0] for d in data_CV]
        
        if len(v_CC) < num_v:
            print(f"第{index+1}组数据的电压数据不足，跳过")
            continue
        if len(i_CV) < num_i:
            print(f"第{index+1}组数据的电流数据不足，跳过")
            continue
        
        voltage_CC.append(v_CC[-num_v:])
        current_CV.append(i_CV[:num_i])
        valid_labels.append(labels[index])

    print("-" * 50)

    return voltage_CC, current_CV, valid_labels


def get_vCC_iCV(curves, Vl, Il):
    voltage_CC = []
    current_CV = []
    for index, curve in enumerate(curves):
        if len(curve["stages"]) < 5:
            print(f"第{index+1}组数据不完整，跳过；它的stages是：")
            print(curve["stages"])
            continue
        CC = curve["stages"][Stage.CC_IN.value]
        CV = curve["stages"][Stage.CV_IN.value]
        data_CC = curve["data"][CC[0] : CC[1]]
        data_CV = curve["data"][CV[0] : CV[1]]
        v_CC = [d[1] for d in data_CC]
        i_CV = [d[0] for d in data_CV]
        idx_vl = get_closest_idx(np.array(v_CC), Vl)
        idx_il = get_closest_idx(np.array(i_CV), Il)
        voltage_CC.append(v_CC[idx_vl:])
        current_CV.append(i_CV[:idx_il])

    print("-" * 50)

    return voltage_CC, current_CV


def read_capacity_data(capacity_code):
    true_capacity = np.load(f"{capacity_code}/true_capacity.npy")
    pred_capacity = np.load(f"{capacity_code}/pred_capacity.npy")
    print(f"True capacity shape: {true_capacity.shape}")
    print(f"Pred capacity shape: {pred_capacity.shape}")
    print("-" * 50)
    return true_capacity, pred_capacity
