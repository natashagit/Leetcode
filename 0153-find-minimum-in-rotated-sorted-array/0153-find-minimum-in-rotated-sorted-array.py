class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity = O(lgn)
        n = len(nums)
        low = 0
        high = n-1
        min_val = float("inf")
        while (low<=high):
            mid = (low+high)/2
            # check if left or right sorted
            if nums[low]<=nums[mid]:
                # In sorted left half
                min_val = min(nums[low], min_val)
                low = mid+1
            else:
                # In sorted right half
                min_val = min(nums[mid], min_val)
                high = mid-1
        return min_val
            




        # Time complexity = O(n)
        # min_val = float("inf")
        # for i in range(len(nums)):
        #     min_val = min(nums[i],min_val)
        # return min_val
