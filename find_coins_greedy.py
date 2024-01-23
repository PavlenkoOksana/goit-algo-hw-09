def find_coins_greedy(amount, coins):
    sorted_coins = sorted(coins, reverse=True)
    result = {coin: 0 for coin in coins}

    for coin in sorted_coins:
        if amount // coin > 0:
            result[coin] = amount // coin
            amount = amount - result[coin] * coin

    return result


def find_coins_greedy_print(dict):
    print("Покупцеві потрібно повернути суму наступними монетами: \n")
    for key, value  in dict.items():
        if value != 0:
            print(f"номінал монети {key}: кількість {value}")


def main():
    amount = 11
    coins = [1, 2, 5, 10, 25, 50]
    res = find_coins_greedy(amount,coins)
    find_coins_greedy_print(res)
    
if __name__ == "__main__":
    main()