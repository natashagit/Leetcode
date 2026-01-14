class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        path = []
        dict_nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(i):
            if i==len(digits):
                result.append("".join(path))
                return
            letters = dict_nums[digits[i]]
            for ch in letters:
                path.append(ch)
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return result