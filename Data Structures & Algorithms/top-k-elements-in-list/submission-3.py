class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_freq = max(freq.values())
        buckets = [[] for i in range(max_freq + 1)]
        for i, j in freq.items():
            buckets[j].append(i)
        sol = []
        for i in buckets:
            sol.extend(i)

        return sol[-k:]