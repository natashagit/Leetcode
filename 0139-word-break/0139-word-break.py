class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # wordDict = {"cats","dog","sand","and","cat"}
        #     c    a      t      s      a      n          d        o         g 
        #    0     1      2       3     4      5        6          7         8     9
        # [True  False  False   True  True    False     False     True    False   False]
        #                                                                    i
        #    j                              

        wordDict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j]==True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

        