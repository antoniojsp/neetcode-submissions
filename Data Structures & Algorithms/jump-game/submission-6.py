class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, j in enumerate(nums):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i+j)
        return True
        