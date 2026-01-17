class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i]=='*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                elif star:
                    star.pop()
                
        while left and star:
            if left.pop()>star.pop():
                return False
        return not left