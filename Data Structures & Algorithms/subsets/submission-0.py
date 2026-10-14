class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def dfs(start):
            res.append(sub.copy())
            for i in range(start, len(nums)):
                sub.append(nums[i])
                dfs(i+1)
                sub.pop()
        
        dfs(0)
        print(res, sub)

        return res