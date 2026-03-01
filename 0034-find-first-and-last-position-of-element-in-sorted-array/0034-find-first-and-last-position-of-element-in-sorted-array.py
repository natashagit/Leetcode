class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        def firstSearch(l,r):
            while l<r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                else: 
                    r = mid
            return l if nums[l]==target else -1
        first = firstSearch(0, len(nums)-1)

        def lastSearch(l, r):
            while l<r:
                mid = (l+r+1)//2
                if nums[mid]>target:
                    r = mid-1
                else:
                    l = mid
            return r if nums[r]==target else -1
        last = lastSearch(0, len(nums)-1)   
        return [first, last]