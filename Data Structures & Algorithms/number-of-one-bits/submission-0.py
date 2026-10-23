class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bitmask = 1
        res = 0
        i = n
        while n > 0:
            print(f"{bitmask:032b}" )
            print(f"{n:032b}" )
            print(f"{(bitmask & n):032b}" )
            print("hjere")
            if (bitmask & n) == 1:
                res+=1
            n>>=1
            # bitmask <<=1

        return res