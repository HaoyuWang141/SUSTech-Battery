import pickle
import scipy.signal

# 从文件中加载对象
with open("EIS5.pickle", "rb") as f:
    EIS5 = pickle.load(f)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_eis_3d(EIS_list):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for eis in EIS_list:
        ax.scatter(
            eis["Re"], [eis["cycle"]] * len(eis["Re"]), eis["-Im"], s=0.5, color="b", alpha=0.2
        )
        # peaks = scipy.signal.find_peaks_cwt(eis["-Im"], 3)
        # print(peaks)
        peak = 29
        ax.scatter(
            eis["Re"][peak],
            eis["cycle"],
            eis["-Im"][peak],
            s=10,
            color="r",
        )
        valley = 42
        ax.scatter(
            eis["Re"][valley],
            eis["cycle"],
            eis["-Im"][valley],
            s=10,
            color="g",
        )

    ax.set_title("EIS Curve (3D)", fontsize=18)
    ax.set_xlabel("Re(Z)", fontsize=16, labelpad=20)
    ax.set_ylabel("Cycle", fontsize=16, labelpad=20)
    ax.set_zlabel("-Im(Z)", fontsize=16, labelpad=20)

    ax.xaxis.set_label_position("lower")
    ax.yaxis.set_label_position("lower")
    ax.zaxis.set_label_position("upper")

    ax.invert_xaxis()

    ax.grid(True)
    ax.set_axis_on()

    plt.show()


plot_eis_3d(EIS5[0:125])
