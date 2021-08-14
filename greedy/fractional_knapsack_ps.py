# 부분 배낭 문제 (fractional knapsack problem)

def fkp(data_list, capacity):
    # 무게대비 가치가 높은 순으로 정렬
    data_list = sorted(data_list, key=lambda x: x[1]/ x[0], reverse=True)
    total_value = 0
    total_detail = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1] # 가치 저장

            total_detail.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0] # 일부 무게 비율만큼
            total_value += data[1] * fraction

            total_detail.append([data[0], data[1], fraction])
            break

    return total_value, total_detail

if __name__ == '__main__':
    # [(무게, 가치)]로 이루어진 n개의 물건
    # capacity에 물건의 무게만큼 전부 넣을 수 있으면 100%의 가치를 저장
    # capacity보다 물건의 무게가 많이나가면 물건의 일부 가치만 저장
    data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
    print(fkp(data_list, 30))