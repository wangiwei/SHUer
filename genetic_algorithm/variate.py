import random
import numpy as np


def variate(z, iter, population, demand, facility, variation, iteration):
    """
    变异过程，单点编译与多点变异交叉进行
    :param z:
    :return: z: 变异后的种群
    """

    for pop in range(0, population, 2):

        if random.random() < variation:

            # 变异个体
            pop_idx = random.randint(0, population-1)

            if iter < iteration / 2:
                # 变异基因位，多点变异
                gen_list = np.random.choice(demand-1, random.randint(0, 5), replace=False)
                for i in gen_list:
                    z[pop_idx, i*2] = random.randint(0, facility-1)
                    z[pop_idx, i*2+1] = 180

            else:
                # 单点变异
                if random.random() > 0.5:
                    gen_position = random.randint(0, demand-1)
                    z[pop_idx, gen_position*2] = random.randint(0, facility-1)
                    z[pop_idx, gen_position*2+1] = 180
                else:
                    # 层级交换
                    gen_position = random.randint(0, demand-1)
                    trans_gen = z[pop_idx, gen_position*2]
                    z[pop_idx, gen_position*2] = z[pop_idx, gen_position*2+1]
                    z[pop_idx, gen_position*2+1] = trans_gen

    return z

