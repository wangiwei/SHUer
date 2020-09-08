import matplotlib.pyplot as plt
import random
import time
from genetic_algorithm.data import *
from genetic_algorithm.fitness import fitness
from genetic_algorithm.select import select
from genetic_algorithm.cross import cross
from genetic_algorithm.variate import variate



# algorithm parameters
population = 200
iteration = 1000
variation = 0.2
crossover = 0.6

average_value = np.zeros(iteration)
best_solution = np.zeros(demand * level)
best_value = np.zeros(iteration)


# 需求调节
alpha = 0.7
h3 = np.zeros(demand)
for i in range(demand):
    h3[i] =  alpha * h1[i] + (1 - alpha) * h2[i]

# 生成初始解，优先使用已建设施点，再考虑拟建设施点
z = np.zeros((population, demand * level))
for pop in range(population):
    for i in range(demand):
        min_dis = min(distance[i, :, 0])
        if random.random() > 0.3:
            # 180 标记某一需求点某一层未分配
            z[pop, i * 2] = distance[i, :, 0].tolist().index(min_dis)
            z[pop, i * 2 + 1] = 180
        else:
            z[pop, i * 2] = 180
            z[pop, i * 2 + 1] = distance[i, :, 0].tolist().index(min_dis)

# 随机分配
# for pop in range(population):
#     for i in range(demand):
#         if random.random() > 0.1:
#             z[pop, i*2] = random.randint(0, 178)
#             z[pop, i*2+1] = 180
#         else:
#             z[pop, i * 2] = 180
#             z[pop, i * 2 + 1] = random.randint(0, 178)

# start
start_time = time.time()
iter = 0
while iter < iteration:

    # 适应度
    fitness_value = fitness(z, distance, fixed_cost, population, demand, facility, level, h3, capacity)

    best_value[iter] = min(fitness_value)
    average_value[iter] = sum(fitness_value) / population

    # 选择
    z = select(fitness_value, z, population, facility, demand, level, iter)

    # 交叉
    z = cross(z, population, demand, crossover)

    # 变异
    z = variate(z, iter, population, demand, facility, variation, iteration)

    iter = iter + 1

end_time = time.time()

# 画图
plt.plot(range(iteration), best_value, color='red', label='best')
plt.plot(range(iteration), average_value, color='green', label='average')
plt.legend()
plt.show()


