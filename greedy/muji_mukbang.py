# 무지의 먹방 라이브
# food_time만큼의 음식 개수와 각 음식의 타임이 주어질 때 k 시간 후에 먹어야 할 음식 번호는 ?

def get_time(food, k):
    num = 0
    for i in range(k):
        if food.count(0) == len(food):
            return -1

        if i < len(food) and food[i] != 0:
            food[i] -= 1
            print(f'{i}번 음식을 섭취한다. 남은 시간은 {food}입니다.')
            num = i

        elif i >= len(food) and food[i - len(food)] != 0:
            food[i - len(food)] -= 1
            print(f'{i - len(food)}번 음식을 섭취한다. 남은 시간은 {food}입니다.')
            num = i - len(food)

    print(f'{num + 1}번째 음식을 먹을 차례입니다.')
    return num + 1


if __name__ == '__main__':
    print('food time: ', end='')
    food = list(map(int, input().split(' ')))

    print('k: ', end='')
    k = int(input())

    get_time(food, k)