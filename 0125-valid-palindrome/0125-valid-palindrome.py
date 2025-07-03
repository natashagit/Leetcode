class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True