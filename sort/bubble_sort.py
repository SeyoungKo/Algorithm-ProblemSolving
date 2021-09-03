# 버블 정렬
# 반복문이 두개이므로 O(n²), 완전 정렬이 되어있는 상태라면 최선은 O(n)

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

if __name__ == '__main__':
    data = [4, 3, 1, 5, 6]
    print(bubble_sort(data))