class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i]=="[" or s[i]=='{' or s[i]=='(':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                if (s[i]==']' and stack[-1]=='[') or (s[i]=='}' and stack[-1]=='{') or (s[i]==')' and stack[-1]=='('):
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False