class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # input: array with jump lengths
        # output: false/true if the lengths can make one reach the last index
        # recursion approach - O(2^n)
        # def dfs(i):
        #     if i==len(nums)-1:
        #         return True
        #     end = min(len(nums)-1, i+nums[i])
        #     for j in range(i+1, end+1):
        #         if dfs(j):
        #             return True
        #     return False
        # return dfs(0)
        
        # instead of recursive approach use greedy by going in reverse and checking if each position can be reached by previous indices
        # goal can start at end
        # check backwards iteratively each index if summed up is >=goal
        # if so can update goal to that index and check the next
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if (nums[i]+i)>=goal:
                goal = i
        if goal==0:
            return True
        return False


