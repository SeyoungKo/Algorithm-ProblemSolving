# Kth Largest Element in a Stream (703)
import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        if k < len(self.heap):
           heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

if __name__ == '__main__':
    arr = [3, 4, 5, 8, 2]
    k = 3
    kthLargest = KthLargest(k, arr)
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))