import numpy as np
import matplotlib.pyplot as plt

pems08_t80_st2_st1_mae = np.array([16.351, 16.117, 16.240])
pems08_t80_st2_st1_mape = np.array([12.351, 11.877, 11.987])
pems08_t80_st2_st1_rmse = np.array([27.704, 26.633, 26.771])

pems08_t80_st2_full_mae = np.array([14.806, 14.912, 14.937])
pems08_t80_st2_full_mape = np.array([10.039, 10.080, 10.199])
pems08_t80_st2_full_rmse = np.array([23.890, 24.071, 24.095])


def abl_mae_8():
    x = ["80%", "80%*", "None"]
    y = pems08_t80_st2_full_mae
    plt.figure(figsize=(8, 6))
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.rcParams['font.size'] = 18
    axes = plt.axes()
    # axes.set_xlim([4, 8])
    axes.set_ylim([14.5, 15])
    plt.bar(x, y, color=['#39c5bb', '#ffc5bb', '#39ffc5'], width=0.5)
    # plt.title("Eval on PeMSD8", fontsize=25)
    plt.xlabel("Transfer Set", fontsize=18)
    plt.ylabel("MAE", fontsize=18)
    plt.savefig("mae8.jpg")


def abl_mape_8():
    x = ["80%", "80%*", "None"]
    y = pems08_t80_st2_full_mape
    plt.figure(figsize=(8, 6))
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.rcParams['font.size'] = 18
    axes = plt.axes()
    axes.set_ylim([10, 10.25])
    plt.bar(x, y, color=['#39c5bb', '#ffc5bb', '#39ffc5'], width=0.5)
    # plt.title("Eval on PeMSD8", fontsize=25)
    plt.xlabel("Transfer Set", fontsize=18)
    plt.ylabel("MAPE(%)", fontsize=18)
    plt.savefig("mape8.jpg")


def abl_rmse_8():
    x = ["80%", "80%*", "None"]
    y = pems08_t80_st2_full_rmse
    plt.figure(figsize=(8, 6))
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.rcParams['font.size'] = 18
    axes = plt.axes()
    axes.set_ylim([23.75, 24.25])
    plt.bar(x, y, color=['#39c5bb', '#ffc5bb', '#39ffc5'], width=0.5)
    # plt.title("Eval on PeMSD8", fontsize=25)
    plt.xlabel("Transfer Set", fontsize=18)
    plt.ylabel("RMSE", fontsize=18)
    plt.savefig("rmse8.jpg")


if __name__ == "__main__":
    abl_mae_8()
    abl_mape_8()
    abl_rmse_8()
