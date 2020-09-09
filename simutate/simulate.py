import matplotlib.pyplot as plt
import numpy as np
import random
import time
from .data import *
from .fitness import fitness
from .variate_same_temperature import variate_same_temperature


# 需求调节
alpha = 0.7
h3 = np.zeros(demand)
for i in range(demand):
    h3[i] =  alpha * h1[i] + (1 - alpha) * h2[i]

# 算法参数
initial_temp = 1000
final_temp = 0.001
reduce_temp = 0.9
internal_loop = 100

best_value = list()
# 产生随机可行解
z = np.zeros(demand*level)
for i in range(demand):
    if random.random() > 0.4:
        z[i*2] = random.randint(0, facility-1)
        z[i*2+1] = 180
    else:
        z[i*2] = 180
        z[i*2+1] = random.randint(0, facility-1)

start_time = time.time()
i = 0
while initial_temp > final_temp:

    # 等温变异
    z, best_value_under_same_temperature = variate_same_temperature()

    best_value.append(best_value_under_same_temperature)
    initial_temp = initial_temp * reduce_temp
    i = i + 1

end_time = time.time()

# 画图
plt.plot(range(i), best_value, color='red', label='best_value')
plt.legend()
plt.title('SA')
plt.show()

