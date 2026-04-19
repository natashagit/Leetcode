class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs:
                if i == len(word) or word[i]!=prefix[i]:
                    return prefix[:i]
        return prefix

        