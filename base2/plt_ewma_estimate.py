import matplotlib.pyplot as plt
from datetime import datetime
import math


def get_day_int(day):
    day = day[0:9]
    return int(day.replace("-", ""))

t_init = 0
e_init = 0
alpha = 0.5

c_dict = {}

x = []
y = []

x_com = []
y_com = []

day = 1

with open('sorted_result.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if (len(parts) >= 2):
            c_time = parts[0]
            bias = int(parts[1])
            if ((len(x) == 0) or (x[-1] != c_time)):
                x.append(c_time)
                y.append(bias)
            else:
                y[-1] += bias
print(x)

for i in range(len(y)):
    y[i] = y[i] / 100000

cur_day = get_day_int(x[0])
i = 0

while i < len(x):
    j = i
    while (j < len(x)) and (get_day_int(x[j]) < day + cur_day):
        j = j + 1
    t = 0
    for k in range(i,j):
        t = t + y[k]
    x_com.append(x[i])
    y_com.append(t)
    i = j
    cur_day = cur_day + day
    
print(len(x_com))

y_com[0] = y_com[0]/2

for i in range(1,len(y_com)):
    cur = y_com[i]
    prev = y_com[i-1]
    y_com[i] = cur * alpha + (1 - alpha) * prev
    print (y_com[i])
    

plt.xlabel("Time")
plt.ylabel("EWMA Estimation")
plt.plot(x_com,y_com)
plt.show()
