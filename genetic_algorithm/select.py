import numpy as np


def select(fitness_value, z, population, facility, demand, level, iter):
    """
    输入该代种群适应度值，经过*轮盘赌*和精英选择返回下一代基因种群
    :param fitness_value:  上一代种群适应度值
    :param z: 上一代种群染色体
    :return: new_Z :下一代种群适应度值
    """

    fitness_value_frace = np.zeros(population)
    ratio = np.zeros(population)
    new_z = np.zeros((population, demand*level))

    for pop in range(population):
        fitness_value_frace[pop] = 1 / fitness_value[pop]

    for pop in range(population):
        ratio[pop] = fitness_value_frace[pop] / sum(fitness_value_frace)

    select_pop_idx = np.random.choice(population, population-1, replace=True, p=ratio)

    for pop in range(population-1):
        new_z[pop, :] = z[select_pop_idx[pop], :]

    best_idx = fitness_value.tolist().index(min(fitness_value))
    new_z[population-1, :] = z[best_idx, :]

    print('-------------这是第{}代---------'.format(iter+1))
    print('最优值为', fitness_value[best_idx])
    print('最优解为', z[best_idx, :])

    return new_z