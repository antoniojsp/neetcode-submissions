from heapq import heappush, nlargest, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.heap = nums[::]
        self.nth = k

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        return nlargest(self.nth, self.heap)[-1]