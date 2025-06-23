class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt= 0
        i = 0
        
        while i<len(s):
            #odd
            l = r = i
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    cnt+=1
                    l-=1
                    r+=1
                else:
                    break
            i+=1
        i=0
        while i<len(s):
            # even
            l = i
            r = i+1
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    cnt+=1
                    l-=1
                    r+=1
                else:
                    break
            i+=1
        return cnt