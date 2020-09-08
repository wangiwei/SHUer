import random

def cross(z, population, demand, crossover):
    """
    交叉函数：种群中多个体两点交叉
    :param z: I*J*K，分配变量
    :return: z: 交叉后的个体
    """

    for pop in range(0, population, 2):

        if random.random() < crossover:

            # 交叉个体
            pop_one = random.randint(0, population-1)
            pop_two = random.randint(0, population-1)
            if pop_one != pop_two:
                # 交叉个体编号不同
                min_pop = min(pop_one, pop_two)
                max_pop = max(pop_one, pop_two)

                # 基因位置
                gen_one = random.randint(0, demand-1)
                gen_two = random.randint(0, demand-1)

                if gen_one == gen_two:
                    # 两点交叉
                    for gen in range(gen_one*2, (gen_one+1)*2):
                        trans_gen = z[min_pop, gen]
                        z[min_pop, gen] = z[max_pop, gen]
                        z[max_pop, gen] = trans_gen
                else:
                    # 片段交叉
                    min_gen = min(gen_one, gen_two)
                    max_gen = max(gen_one, gen_two)
                    for gen in range(min_gen*2, (max_gen+1)*2):
                        trans_gen = z[min_pop, gen]
                        z[min_pop, gen] = z[max_pop, gen]
                        z[max_pop, gen] = trans_gen

    return z

