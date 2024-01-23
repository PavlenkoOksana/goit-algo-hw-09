import timeit
import numpy as np
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def measure_time(func, amount,coins):
    def func_data():
        return func(amount,coins)

    return timeit.timeit(func_data, number=1)

amounts = [57, 113]
num_coins = [3, 5]

greedy_times = []
dp_times = []

for n in num_coins:
    coins = sorted(np.random.randint(1, 50, n))
    for amount in amounts:
        greedy_times.append(measure_time(find_coins_greedy, amount, coins)) 
        dp_times.append(measure_time(find_min_coins, amount, coins)) 

    
print ("greedy_times", greedy_times)
print("dp_times",dp_times)