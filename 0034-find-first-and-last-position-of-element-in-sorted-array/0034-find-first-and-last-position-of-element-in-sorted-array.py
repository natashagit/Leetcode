class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def findFirst(nums, target):
            left = 0
            right = len(nums)-1
            result = -1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    result = mid
                    right = mid-1 # shift to keep searching in left side
                elif target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            return result

        def findLast(nums, target):
            left = 0
            right = len(nums)-1
            result = -1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    result = mid
                    left = mid+1 # shift to keep searching in right side
                elif target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            return result
        
        return [findFirst(nums, target), findLast(nums, target)]
       