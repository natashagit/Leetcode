class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # input: array
        # output: triplets list that sum up to 0 from array
        # no duplicates
        # order doesnt matter
        # less than 3 elements -> []
        # for every possible triplet use 3 nested loops
        # O(n^3)
        # Optimal
        # sort the array [-4, -1, -1, 0, 1, 2]
        # loop through the array 
        # assign the left pointer and right pointer
        # loop while left<right
        # sum up and see if 0
        # if 0 then return the indices
            # move left ahead and check its not equal to prev
        # if >0 move right 
        # if <0 move left
        # O(n^2)
        nums.sort()
        result = []
        for i in range(len(nums)-2): # [-4, -1, -1, 0, 1, 2]
            if i>0 and nums[i-1]==nums[i]:
                continue
            left = i+1 #1
            right = len(nums)-1 #5
            while left<right:
                if nums[left]+nums[right]+nums[i]>0:
                    right-=1
                elif nums[left]+nums[right]+nums[i]<0:
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                    
        return result
        





