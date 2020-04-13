'Single Server Queue Simulation'

from random import expovariate, gauss
from statistics import mean, median, stdev
import math as m

mean_arr_interval = 5.6
mean_serv_time = 2.5
stdev_serv_time = 0.0

num_waiting = 0
arrivals = []
starts = []
serv_q = []
arrival = service_end = 0.0
for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        serv_q.append(num_waiting)
        arrival += expovariate(1.0 / mean_arr_interval)
        arrivals.append(arrival)
    else:
        if num_waiting > 0:
            num_waiting -= 1
        serv_q.append(num_waiting)
        service_start = service_end if num_waiting else arrival
        service_time = gauss(mean_serv_time, stdev_serv_time)
        service_end = service_start + service_time
        starts.append(service_start)
waits = [start - arrival for arrival, start in zip(arrivals, starts)]
print(f'Mean wait: {mean(waits): .1f} Stdev Wait:{stdev(waits):.1f}')
print(f'Median wait: {median(waits):.1f} Max Wait: {max(waits):.1f}')
print(f'Server Queue Len: {m.ceil(mean(serv_q))} Stdev Wait:{stdev(serv_q)}')
