def find_min_coins(amount, coins):
    # Створення та ініціалізація таблиці для зберігання кількості монет для кожної суми
    dp_table = [float('inf')] * (amount + 1)
    dp_table[0] = 0  # Нульова кількість монет потрібна для видачі 0

    # Перебір сум від 1 до amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp_table[i - coin] + 1 < dp_table[i]:
                dp_table[i] = dp_table[i - coin] + 1

    # Побудова результату (списку монет та їх кількості)
    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        for coin in coins:
            if remaining_amount >= coin and dp_table[remaining_amount - coin] + 1 == dp_table[remaining_amount]:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                remaining_amount -= coin
                break

    return result


def main():
    amount = 113
    coins = [1, 2, 5, 10, 25, 50]
    result = find_min_coins(amount, coins)
    print(result)


if __name__ == "__main__":
    main()