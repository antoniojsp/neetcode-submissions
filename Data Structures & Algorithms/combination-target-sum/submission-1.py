class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(start, curr):
            if curr == target:
                res.append(sub.copy())
                return 

            if curr > target:
                return

            for i in range(start, len(nums)):
                sub.append(nums[i])
                dfs(i, curr + nums[i])
                sub.pop()
        dfs(0, 0)

        return res