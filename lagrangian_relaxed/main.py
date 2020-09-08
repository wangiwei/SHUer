from lagrangian_relaxed.data import *
import numpy as np
import matplotlib.pyplot as plt
import time


lambda_ = np.zeros(facility) # 拉格朗日乘子
same_limit = 5
scale = 0.8
iteration = 100
z = np.zeros(demand, facility, level)
x = np.zeros(facility)
demanding = np.zeros(demand)

# 调和需求点人口数量
for i in range(demand):

    demanding[i] = 0.7 * h1[i] + 0.3 * h2[i]

# 初始化乘子，求解 FLSP 模型
for fac in range(facility):

    lambda_[fac] = min(distance[:, fac, 0]) * 2

    if fixed_cost[fac] - lambda_[fac] * capacity[fac] < 0:

        x[fac] = 1

# 求解 CASP 模型
for i in range(demand):
    real_dist_first = dict()
    real_dist_second = dict()
    for j in range(facility):
        if x[j] == 1:
            real_dist_first[j] = distance[i, j, ]





