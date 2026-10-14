class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_freq = max(freq.values())
        buckets = [[] for i in range(max_freq + 1)]
        for i, j in freq.items():
            buckets[j].append(i)
        sol = []
        for i in range(len(buckets)-1,0, -1):
            for num in buckets[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol
        return sol