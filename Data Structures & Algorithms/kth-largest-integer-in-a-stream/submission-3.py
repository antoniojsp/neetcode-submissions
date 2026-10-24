from heapq import heappush, nlargest, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[::]
        heapify(self.heap)
        self.nth = k

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        return nlargest(self.nth, self.heap)[-1]