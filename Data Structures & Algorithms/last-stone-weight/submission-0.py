
from heapq import heapify_max, heappush_max, heappop_max

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            first, second = heappop_max(stones), heappop_max(stones)
            result = first - second
            if result > 0:
                heappush_max(stones, result)
            
        print(stones)
        return stones.pop() if stones else 0
