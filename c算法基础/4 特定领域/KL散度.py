# 手写一个函数可以实现 KL 的散度的计算过程

import numpy as np
import math

def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

p = np.array([0.36, 0.48, 0.16])
q = np.array([0.333, 0.333, 0.333])
print(kl_divergence(p, q))  # 0.085299