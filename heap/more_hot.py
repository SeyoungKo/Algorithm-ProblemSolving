# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        min_val1 = heapq.heappop(scoville)
        
        if min_val1 >= K:
            break
        if len(scoville) <= 0:
            return -1
        
        min_val2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_val1 + min_val2 * 2)
        answer += 1
    return answer


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))
