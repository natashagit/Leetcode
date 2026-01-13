class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # input: list of nums
        # output: all possible subsets of nums: O(n2^n)
        # see all possible options using tree and dfs by backtracking
        result = []
        path = []
        # i -> index of nums
        def dfs(i):
            # base case to store the path
            if i==len(nums):
                result.append(path[:])
                return
            
            # skip nums[i]
            dfs(i+1)

            # keep nums[i]
            path.append(nums[i])
            dfs(i+1)
            # Need to backtrack to previous state 
            path.pop()
        dfs(0)
        return result