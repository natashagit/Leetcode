class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 2 6
        # 1 1+1 1+2
        if s[0]=='0':
            return 0
        nums = [0]*len(s)
        nums[0] = 1
        for i in range(1, len(s)):
            if s[i]!='0':
                nums[i]+=nums[i-1]
            if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                if i>=2:
                    nums[i]+=nums[i-2]
                else: 
                    nums[i]+=1
        
        return nums[-1]
