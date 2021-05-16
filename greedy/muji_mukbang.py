# 무지의 먹방 라이브
# food_time만큼의 음식 개수와 각 음식의 타임이 주어질 때 k 시간 후에 먹어야 할 음식 번호는 ?
import headq

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

# 시간이 적게 걸리는 음식부터 확인해서 제거해나간다. (우선순위 큐)
def get_time_priorityQ(food, k):
    # phase1. k - (음식의 개수 * 시간이 가장 적게 걸리는 음식을 먹는 시간)
    # phase2. 갱신된 k에서 다음으로 시간이 적게 걸리는 음식을 먹는 시간으로 계산

    # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1
    if sum(food) <= k:
        return -1

    q = []
    for i in range(len(food)):
        headq.headpush(q, (food[i], i+1)) # 음식 시간, 음식 번호

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food) # 남은 음식 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = headq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중 몇번째 음식인지 확인
    result = sorted(q, key=lambda x: x[1]) # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length[1]]


if __name__ == '__main__':
    print('food time: ', end='')
    food = list(map(int, input().split(' ')))

    print('k: ', end='')
    k = int(input())

    get_time(food, k)
    get_time_priorityQ(food, k)