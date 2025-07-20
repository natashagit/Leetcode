class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

        #       0   h   e   l   l   o   w   o   r   l   d 
        # dp = [T   F   T   F   T   T   F   F   F   F   T]
        #                               j               i
        # wordDict = ['he', 'world', 'ello', 'he', 'lo', 'll']