class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # input: nums
        # output: true/false if triplet i<j<k exists
        # [2,1,5,0,4,6]
                # i j k
        nums_i = float("inf")
        nums_j = float("inf")
        for num in nums:
            if num<=nums_i:
                nums_i = num
            elif num<=nums_j:
                nums_j = num
            else:
                return True
        return False
         
        