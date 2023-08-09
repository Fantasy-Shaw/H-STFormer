import torch
import numpy as np

if __name__ == "__main__":
    str1 = "PeMS04ST60"
    print(str1[:6])

    ts = torch.zeros(4, 4)
    print(ts)

    arr1: np.ndarray = np.array(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    )
    arr2: np.ndarray = np.array(
        [11, 12, 13]
    )
    print(arr1[1][0], arr1[1][1], arr1[1][2])
    arr1[1] = arr2
    print(arr1)
    print(arr2[0:2])

    tp1 = (114514, 1919810, 12345, 114, 514)
    print(min(tp1))
