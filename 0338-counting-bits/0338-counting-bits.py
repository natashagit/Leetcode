class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cnt = 0
        ans = []
        for k in range(n+1):
            while (k>0):
                if k%2!=0:
                    cnt+=1
                k = k//2
            ans.append(cnt)
            cnt = 0
        return ans
        
