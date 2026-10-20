def digits(num):
    res = 0
    while num > 0:
        res+=(num%10)**2
        num//=10
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1:
            n = digits(n)
            if n in seen:
                return False
            seen.add(n)
        return True