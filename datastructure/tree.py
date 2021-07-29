# 트리
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            # 왼쪽
            if value < self.current_node.value:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            # 오른쪽
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            # 왼쪽으로 이동
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            # 오른쪽으로 이동
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        existed = False # 삭제할 노드가 존재하는지 여부
        self.current_node = self.head
        self.parent = self.head # 삭제할 노드 위의 부모 노드

        # 0. 삭제할 노드가 존재하는지 판단 (존재하지 않으면 종료)
        while self.current_node:
            if self.current_node.value == value:
                existed = True
                break
            elif value < self.current_node.value:
                # 왼쪽
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if existed is False:
            return existed

        # 1. 삭제할 노드가 leaf node인 경우
        if self.current_node.left is None and self.current_node.right is None:
            if value < self.parent.value:
                # 왼쪽
                self.parent.left = None
            else:
                # 오른쪽
                self.parent.right = None
            del self.current_node

        # 2. 삭제할 노드의 child node가 한 개 있는 경우
        # 2.1. child node가 left에 있는 경우
        if self.current_node.left is not None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        # 2.2 child node가 right에 있는 경우
        elif self.current_node.right is not None and self.current_node.left is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 3. 삭제할 노드가 child node를 두 개 가지고 있는 경우

        # 3.1 삭제할 노드가 부모 노드의 왼쪽에 있는 경우
        # 3.1.1 삭제할 노드가 부모 노드의 왼쪽에 있고, 삭제할 노드의 오른쪽 child node 중
        # 3.1.1 삭제할 노드가 부모 노드의 왼쪽에 있고 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 child node가 없을 때
        # 3.1.2 삭제할 노드가 부모 노드의 왼쪽에 있고 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 오른쪽에 child node가 있을 때
        # (가장 작은 값을 가진 노드의 child node가 왼쪽에 있을 수는 없음 -> 왼쪽 노드에 있다는 것은 해당 노드보다 더 작은 값을 가지는 노드가 있다는 뜻이기 때문)

        # 3.2 삭제할 노드가 부모 노드의 오른쪽에 있는 경우
        # 3.2.1 삭제할 노드가 부모 노드의 왼쪽에 있고 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 child node가 없을 때
        # 3.2.2 삭제할 노드가 부모 노드의 왼쪽에 있고 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 오른쪽에 child node가 있을 때
        # (가장 작은 값을 가진 노드의 child node가 왼쪽에 있을 수는 없음 -> 왼쪽 노드에 있다는 것은 해당 노드보다 더 작은 값을 가지는 노드가 있다는 뜻이기 때문)
if __name__ == '__main__':
    head = Node(1)
    bst = BinarySearchTree(head)
    bst.insert(2)
    bst.insert(3)
    bst.insert(6)
    bst.insert(8)

    print(bst.search(10))
