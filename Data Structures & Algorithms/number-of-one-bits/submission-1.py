class Solution:
    def hammingWeight(self, n: int) -> int:
        bitmask = 1
        res = 0
        while n > 0:
            if (bitmask & n) == 1:
                res+=1
            n>>=1

        return res