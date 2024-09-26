# 实现 AUC 的计算，利用排序的方式来计算
# 数据包括：真实标签，预测标签
# 生成对应的标签和对应的预测分布值，阈值这里取 0.5

import numpy as np
import pandas as pd

# 生成数据
np.random.seed(0)
y_true = np.random.randint(0, 2, 1000)
y_pred = np.random.rand(1000)

print(y_true)
print(y_pred)

# 计算 AUC
def AUC(y_true, y_pred):
    len_pos = np.sum(y_true)
    len_neg = len(y_true) - len_pos
    # 生成的分母包括
    total_case = len_pos * len_neg
    res = 0
    for i in range(len(y_true)):
        if y_true[i] == 1:
            for j in range(len(y_true)):
                if y_true[j] == 0 and y_pred[j] > y_pred[i]:
                    res += 1
    return res / total_case

print(AUC(y_true, y_pred))


# 求平方根
target = 0.5
# 