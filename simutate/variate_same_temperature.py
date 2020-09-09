import random
import numpy as np
from .fitness import fitness


def variate_same_temperature(z, d, f, demand, facility, level, h3, capacity, internal_loop, initial_temp):
    """
    等温退火过程，即：在同一温度水平下，金属粒子因充分流动产生变异的现象。
    :param z: 变异前解决方案
    :param d: 配送距离
    :param f: 设施建设成本
    :param demand: 需求点
    :param facility: 设施点
    :param level: 层级数
    :param h3: 调和需求
    :param capacity: 容量约束
    :param internal_loop: 等温内循环
    :param initial_temp: 初始温度
    :return:
        z: 变异后解决方案,
        best_value_under_same_temperature: 该温度下最优解决方案
    """

    best_value_under_same_temperature = fitness(z, d, f, demand, facility, level, h3, capacity)

    for loop in range(internal_loop):

        # 变异
        if initial_temp > 500:
            gen_list = np.random.choice(range(demand), random.randint(1, demand/2), replace=False)
            if len(gen_list) % 2 == 0:

            else:



        else:
            """
            温度下降到500℃，考虑到算法收敛，进行单点变异；
            单点变异分两种：
                - 单点基因位就近替换
                - 单点基因位交叉互换
                - 单点基因位层级互换
            """
            gen = random.randint(0, demand - 1)
            if 0.2 < random.random() < 0.8:

                if z[gen*2] == 180:
                    z[gen*2] = d[gen, :, 0].tolist().index(min(d[gen, :, 0]))
                    z[gen*2+1] = 180
                else:
                    gen_two = random.randint(0, demand-1)
                    if  gen_two != gen:
                        # 交叉互换
                        for k in range(level):
                            trans_gen = z[gen*2+k]
                            z[gen*2+k] = z[gen_two*2+k]
                            z[gen_two*2+k] = trans_gen
            else:
                trans_gen = z[gen*2]
                z[gen*2] = z[gen*2+1]
                z[gen*2+1] = trans_gen

    return z, best_value_under_same_temperature