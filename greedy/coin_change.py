def coin():
    n = 1260
    count = 1
    coin_type = [500, 100, 50, 10]

    for coin in coin_type:
        n -= coin
        if n >= coin:
            while n >= coin:
                n -= coin
                count += 1
        print("{} 거스름돈 개수 : {}".format(coin, count))
        count =1


def best_answer():  # ?? 뭔지 모르겠
    n = 1260
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += coin // coin
        n %= coin
    print(count)

if __name__ == '__main__':
    coin()