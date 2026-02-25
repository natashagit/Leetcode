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
        # left and right pointer
        l = r = 0 
        output = []
        # moving right pointer ahead
        while r<len(nums):
            # while q is not empty and the value being pushed>previous existing value
            while q and nums[q[-1]]<nums[r]:
                # remove previous smaller value and append index of new one
                q.pop()
            q.append(r)
            # if the left pointer moved ahead of window size
            if l>q[0]:
                # remove left val from window
                q.popleft()
            # if window size achieved then add the max value which is at start of queue to the output array
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output