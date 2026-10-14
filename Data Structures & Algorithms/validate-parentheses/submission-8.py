class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapa = {"]":"[", "}":"{", ")":"("}
        for i in s:
            if i in mapa: # closing 
                if not stack:
                    return False
                elif mapa[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
