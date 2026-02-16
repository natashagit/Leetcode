class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # input: array of 3 colored elements
        # output: sorted together inorder of 0, 1, 2
        # loop through with i
        # L and R pointer - shift all elements to left of L that are 0 and all elements to right of R that are 2

        L = 0
        R = len(nums)-1
        i = 0
        while i<=R:
            if nums[i]==0:
                nums[L], nums[i]=nums[i], nums[L]
                L+=1
            elif nums[i]==2:
                nums[R], nums[i]=nums[i], nums[R]
                R-=1
                i-=1 # needs to check swapped element
            i+=1
        return nums