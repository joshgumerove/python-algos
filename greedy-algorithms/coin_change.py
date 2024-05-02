def coin_change(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins) - 1
    count = 0
    while True:
        coin_value = coins[index]
        if N >= coin_value:
            count += 1
            print(coin_value)
            N -= coin_value
        if N < coin_value:
            index -= 1

        if N == 0:
            return print(f"total coins needed {count}")


coins = [1, 2, 5, 20, 50, 100]

coin_change(201, coins)
