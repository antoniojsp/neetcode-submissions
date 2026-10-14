class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(left, right):
            if left > right:
                return -1
            mid  = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return helper(left, mid -1)
            else:
                return helper(mid+1, right)
        return helper(0, len(nums) - 1)
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid  = left + (right - left)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return -1