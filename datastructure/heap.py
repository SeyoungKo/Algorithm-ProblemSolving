# 힙 구현


class Heap:
    def __init__(self, data):
        self.heap_arr = list()
        self.heap_arr.append(None)  # root 노드의 인덱스를 1로 하기 위해 0번째 인덱스를 None으로
        self.heap_arr.append(data)

    def check_node(self, idx):
        if idx <= 1:
            return False
        # 채워진 노드 위치에서 부모 노드보다 값이 클 경우 부모 노드와 위치를 바꿔주는 작업을 반복
        parent_idx = idx // 2
        if self.heap_arr[parent_idx] < self.heap_arr[idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_arr) == 0:
            self.heap_arr.append(None)  # root 노드의 인덱스를 1로 하기 위해 0번째 인덱스를 None으로
            self.heap_arr.append(data)
            return True

        # 삽입할 데이터가 Max Heap의 데이터보다 클 경우
        self.heap_arr.append(data)
        last_idx = len(self.heap_arr) - 1
        while self.check_node(last_idx):
            # 채워진 노드 위치에서 부모 노드보다 값이 클 경우 부모 노드와 위치를 바꿔주는 작업을 반복
            parent_idx = last_idx // 2
            self.heap_arr[parent_idx], self.heap_arr[last_idx] = self.heap_arr[last_idx], self.heap_arr[parent_idx]
            last_idx = parent_idx

        return True

    # 루트 노드 값이 자식 노드보다 작을 경우 자식 노드 중 가장 큰 값과 루트 노드 위치를 바꿔주는 작업을 반복
    def move_down(self, poped_idx):
        pass

    def delete(self):
        # 최상단 노드 (root 노드)를 삭제하는 것이 일반적
        if len(self.heap_arr) <= 1:
            return None
        pop_root = self.heap_arr[1] # 최상단 노드를 삭제
        self.heap_arr[1] = self.heap_arr[-1] # 가장 하위에 있는 노드를 루트 위치로 옮기기
        poped_idx = 1

        while self.move_down(poped_idx): # 루트 노드 값이 자식 노드보다 작을 경우 자식 노드 중 가장 큰 값과 루트 노드 위치를 바꿔주는 작업을 반복
            pass

        return pop_root

if __name__ == '__main__':
    heap = Heap(15)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(4)
    heap.insert(20)
    print(heap.heap_arr)
