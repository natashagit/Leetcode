class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = int((low+high)/2)
            if target==nums[mid]:
                return mid
            # Check in sorted left half
            if nums[low]<=nums[mid]:
                if target>=nums[low] and target<=nums[mid]:
                    # within left half
                    high = mid-1
                else:
                    # not in left half so update low
                    low =mid+1
            else:
                if target>=nums[mid] and target<=nums[high]:
                    # within right half
                    low = mid+1
                else:
                    # not in right half, move to left half
                    high = mid-1
        return -1

