class Solution:
    def numDecodings(self, s: str) -> int:
        # Initializing
        dp = {len(s):1}
        # Loop backwards
        for i in range(len(s)-1, -1, -1):
            # If digit is 0
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            # If two digit starting with 1 or 2"0-6"
            if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                # take number of ways for two digit number
                dp[i]+= dp[i+2]
        # return total number of ways
        return dp[0]