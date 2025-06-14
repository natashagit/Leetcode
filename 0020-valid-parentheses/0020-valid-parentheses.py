class Solution:
    def isValid(self, s: str) -> bool:
        dict_parenthesis = {')':'(',']':'[','}':'{'}
        stack = []

        for char in s:
            if char in dict_parenthesis:
                if stack and stack[-1]==dict_parenthesis[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True