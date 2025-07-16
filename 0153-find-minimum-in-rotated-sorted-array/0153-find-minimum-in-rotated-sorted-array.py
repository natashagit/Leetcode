class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        ult = float("inf")
        while low<=high:
            mid = int((low+high)/2)
            if nums[low]<=nums[mid]:
                # sorted left half
                ult = min(ult,nums[low])
                low = mid+1
            else:
                # sorted second half
                ult = min(ult,nums[mid])
                high = mid-1
        return ult
        


        