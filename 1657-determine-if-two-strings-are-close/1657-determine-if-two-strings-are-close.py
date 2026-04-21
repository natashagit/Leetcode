class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter
        if sorted(Counter(word1).keys())!=sorted(Counter(word2).keys()):
            return False
        return (sorted(Counter(word1).values())==sorted(Counter(word2).values()))

