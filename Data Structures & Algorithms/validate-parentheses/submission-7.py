class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapa = {"]":"[", "}":"{", ")":"("}
        for i in s:
            print(stack)
            if i in mapa: # closing 
                print("cierre")
                if not stack:
                    return False
                if mapa[i] == stack[-1]:
                    print("same")
                    stack.pop()
                else:
                    print("diff")
                    return False
            else:
                stack.append(i)

        return len(stack) == 0
