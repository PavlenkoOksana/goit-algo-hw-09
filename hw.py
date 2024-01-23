import timeit
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def measure_time(func, amount,coins):
    def func_data():
        return func(amount,coins)

    return timeit.timeit(func_data, number=1)


amount_1 = 1056
coins_1 = [1, 2, 5, 10, 25, 50]
res_find_coins_greedy = find_coins_greedy(amount_1,coins_1)
print ("find_coins_greedy",res_find_coins_greedy)
print("measure_time",measure_time(find_coins_greedy,amount_1,coins_1))
res_find_min_coins = find_min_coins(amount_1,coins_1)
print ("find_min_coins",res_find_min_coins)
print("measure_time",measure_time(find_min_coins,amount_1,coins_1))

amount_2 = 113
coins_2 = [1, 2, 5]
res_find_coins_greedy = find_coins_greedy(amount_2,coins_2)
print ("find_coins_greedy",res_find_coins_greedy)
print("measure_time",measure_time(find_coins_greedy,amount_2,coins_2))
res_find_min_coins = find_min_coins(amount_2,coins_2)
print ("find_min_coins",res_find_min_coins)
print("measure_time",measure_time(find_min_coins,amount_2,coins_2))

amount_3 = 1130053
coins_3 = [1, 2, 5, 10, 25, 50]
res_find_coins_greedy = find_coins_greedy(amount_3,coins_3)
print ("find_coins_greedy",res_find_coins_greedy)
print("measure_time",measure_time(find_coins_greedy,amount_3,coins_3))
res_find_min_coins = find_min_coins(amount_3,coins_3)
print ("find_min_coins",res_find_min_coins)
print("measure_time",measure_time(find_min_coins,amount_3,coins_3))

amount_4 = 11300537
coins_4 = [1, 2, 5, 10, 25, 50]
res_find_coins_greedy = find_coins_greedy(amount_4,coins_4)
print ("find_coins_greedy",res_find_coins_greedy)
print("measure_time",measure_time(find_coins_greedy,amount_4,coins_4))
res_find_min_coins = find_min_coins(amount_4,coins_4)
print ("find_min_coins",res_find_min_coins)
print("measure_time",measure_time(find_min_coins,amount_4,coins_4))
    
