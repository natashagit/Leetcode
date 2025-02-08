class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time complexity - O(lgn)
        n = len(nums)
        low = 0
        high = n-1
        while (low<=high):
            mid = (low+high)/2
            # Check if mid value is target
            if target == nums[mid]:
                return mid
            # Check if left half is sorted
            if nums[low]<=nums[mid]:
                # Check if target btwn low and mid
                if target>=nums[low] and target<=nums[mid]:
                    high = mid-1
                else:
                    # if target btwn mid and high
                    low = mid+1
            else:
                # If right half sorted
                if target>=nums[mid] and target<=nums[high]:
                    # if target between mid and high
                    low = mid+1
                else:
                    # if target less than mid
                    high = mid-1
        return -1


        # Time complexity - O(n)
        # for i in range(len(nums)):
        #     if target==nums[i]:
        #         return i
        # return -1