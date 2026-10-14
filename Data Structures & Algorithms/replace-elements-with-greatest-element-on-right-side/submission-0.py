class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        max_value = -1

        for i in arr[::-1]:
            res.append(max_value)
            max_value = max(max_value, i)
        
        return res[::-1]