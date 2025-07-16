class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float("inf")
        low = 0
        high = len(nums)-1
        # Find mid point dynamically
        while (low<=high):
            mid = int((low+high)/2)
            # Check if left half or right half is sorted
            if nums[mid]>=nums[low]:
                # Left half sorted
                min_val = min(min_val, nums[low])
                # Took minimum value in left half, now move to right half
                low = mid+1
            else:
                # Right half sorted
                min_val = min(min_val, nums[mid])
                high =mid-1
        return min_val

        