import numpy as np


def fitness(z, d, f, population, demand, facility, level, h3, capacity):
    """
    计算适应度函数，返回该代种群适应度值
    :param z: population*(I*K) 容量分配方案
    :param d: I*J*K 配送距离
    :param f: J 设施建设成本
    :return: fitness_value
    """

    fitness_value = np.zeros(population)

    for pop in range(population):

        dis_cost = 0
        fac_cost = 0
        unfirst_count = 0
        over_capacity = 0
        punishment_over_capacity = 0
        x = np.zeros(facility)

        # unfirst_count, dis_cost, x
        for i in range(0, demand):

            if z[pop, i*2] == 180: # 首层未分配
                unfirst_count = unfirst_count + 1
                dis_cost = dis_cost + d[i, int(z[pop, i*2+1]), 1]
                x[int(z[pop, i*2+1])] = 1
            else:
                # print('----------z[', pop, ',', i, ']----------', z[pop, i*2])
                dis_cost = dis_cost + d[i, int(z[pop, i*2]), 0]
                x[int(z[pop, i*2])] = 1

        # fac_cost
        for j in range(facility):
            fac_cost = fac_cost + x[j] * f[j]

        # punishment_over_capacity
        for j in range(facility):
            if x[j] == 1:
                demand_amount = list()
                for i in range(demand):
                    if z[pop, i*2] == j or z[pop, i*2+1] == j:
                        demand_amount.append(h3[i])

                if capacity[j] - sum(demand_amount) >= 0:
                    over_capacity = 0
                else:
                    over_capacity = abs(capacity[j] - sum(demand_amount)) * min(d[:, j, 0])

                punishment_over_capacity = punishment_over_capacity + over_capacity

        # 适应度值 = 运输成本 + 设施建设成本 + 非首选成本 + 容量惩罚成本
        fitness_value[pop] = dis_cost + fac_cost + unfirst_count + 10 * punishment_over_capacity

    return fitness_value





