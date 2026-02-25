class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # input: nums, window size k
        # output: max elements in sliding window
        # approach 1: two loops: i to n-k+1 and j=i to i-k+1 and get max; O(n-k)*k TC
        # approach 2: increase from right and shrink from left and keep index of max element in queue
        # init output array
        # l and r ptr = 0
        # loop r till len(nums)
        # while q is not empty and nums[q[-1]]<nums[r] -> q.pop()
        # append r to q to keep the max value in front
        # if l>q[0]-> window moved ahead->q.popleft
        # if r+1>=k-> window size complete so store max in output-> add nums[q[0]] to output array
        # l+=1
        # r+=1
        # return output
        from collections import deque
        q = deque()
        l = r = 0
        output = []
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output