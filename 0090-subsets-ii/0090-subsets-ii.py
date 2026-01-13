class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        path = []
        def backtrack(i):
            result.append(path[:])
            for j in range(i, len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                
                path.append(nums[j])
                backtrack(j+1)
                path.pop()
        backtrack(0)
        return result
        