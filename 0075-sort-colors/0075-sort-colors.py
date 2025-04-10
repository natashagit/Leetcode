class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Using two pointers white and blue
        red = 0
        white = 0
        blue = len(nums)-1
        # red, white, blue colors = 0,1,2
        while white<=blue:
            # Check if white is 0 and red is 1 then switch the two
            if nums[white]==0:
                if nums[red]!=0:
                    nums[red], nums[white] = nums[white], nums[red]
                white+=1
                red+=1
            # If white is 1, then just move ahead
            elif nums[white]==1:
                white+=1
            # If white is 2, then switch with blue if blue is not 2
            else:
                if nums[blue]!=2:
                    nums[white], nums[blue] = nums[blue], nums[white]
                blue-=1
        return nums 


        
