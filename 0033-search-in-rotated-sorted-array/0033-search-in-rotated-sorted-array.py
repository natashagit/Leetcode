class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = int((low+high)/2)
            if target == nums[mid]:
                return mid
            if nums[low]<=nums[mid]:
                # left half sorted
                if nums[low] <= target and target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                # right half sorted
                if nums[mid]<=target and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1