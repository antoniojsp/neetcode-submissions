class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        mapa = {"]":"[", "}":"{", ")":"("}
        for i in s:
            if i in mapa: # closing 
                if stack and mapa[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
