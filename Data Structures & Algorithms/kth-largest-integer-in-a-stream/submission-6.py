from heapq import heappush, nlargest, heapify, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        heapify(self.heap)
        self.nth = k
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.nth:
            print("her")
            heappop(self.heap)
        print(self.heap)
        return nlargest(self.nth, self.heap)[-1]