class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Set count = 0
        count = 0
        n = len(nums)

        # Loop through nums to check if each element is greater than the next, if twice it's greater then not in order
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                #increment to check how many times
                count+=1
                if count>1:
                    return False
        return True