def digits(num):
    res = []
    while num > 0:
        res.append((num%10)**2)
        num//=10
    return sum(res)


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n > 1:
            n = digits(n)
            print(n)
            if n in seen:
                return False
            seen.add(n)

        return True