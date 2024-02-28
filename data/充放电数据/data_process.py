import pandas as pd
import matplotlib.pyplot as plt

# 替换为您的实际Excel文件路径
file_path = "./充放电导出数据.xlsx"

# 创建一个空字典来储存所有工作表的D列和E列数据
sheets_data = {}

cycle_num = 0

# 使用pandas读取Excel文件
with pd.ExcelFile(file_path) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        columns_data = df.iloc[0:, [3, 4]]
        sheets_data[sheet_name] = columns_data
        
for key in sheets_data:
    df = sheets_data[key]
    col1 = df["SOH"]
    
    result = ''
    cnt = 0
    for i in range(9, col1.size, 10):
        result += str(col1[i]) + '\n'
        cnt += 1
    
    print(f'key: {key}, cnt: {cnt}')
        
    with open(f'./capacity {key}.txt', 'w') as f:
        f.write(result)

# for key in sheets_data:
#     df = sheets_data[key]
#     plt.figure()
#     plt.title(f"Charging/Discharging Curve - {key}")

#     plt.subplot(2, 1, 1)
#     plt.plot(df.iloc[:, 0])
#     plt.ylabel("discharging capacity(Ah)")

#     plt.subplot(2, 1, 2)
#     plt.plot(df.iloc[:, 1])
#     plt.ylabel("SOH(%)")
#     plt.xlabel("iteration")

#     plt.show()

#     exit(0)


# for key in sheets_data:
#     df = sheets_data[key]
#     plt.figure(figsize=(10, 6))
#     plt.suptitle(f"Charging/Discharging Curve - {key}")  # 设置整个图形的标题

#     ax1 = plt.subplot(2, 1, 1)  # 第一个子图的轴对象
#     ax1.plot(df.iloc[:, 0])
#     ax1.set_ylabel("Discharging Capacity (Ah)")
#     # 隐藏右侧和顶部的轮廓线
#     ax1.spines["right"].set_visible(False)
#     ax1.spines["top"].set_visible(False)

#     ax2 = plt.subplot(2, 1, 2)  # 第二个子图的轴对象
#     ax2.plot(df.iloc[:, 1])
#     ax2.set_ylabel("SOH (%)")
#     ax2.set_xlabel("Iteration")
#     # 隐藏右侧和顶部的轮廓线
#     ax2.spines["right"].set_visible(False)
#     ax2.spines["top"].set_visible(False)

#     plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # 调整子图布局，为整个图形的标题留出空间
#     plt.show()

#     break  # 使用break而不是exit，以便在显示第一个图形后退出循环
