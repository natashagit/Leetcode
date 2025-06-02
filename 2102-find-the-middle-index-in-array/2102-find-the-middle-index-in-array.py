class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Saving total sum of elements in array
        total = sum(nums)
        # Initially sum of elements to the left of first element is 0
        leftsum = 0
        for i in range(len(nums)):
            # Sum of elements to the right of element 
            rightsum = total - leftsum - nums[i]
            # If the sums are equal return the middle index
            if leftsum==rightsum:
                return i
            # Update the left sum
            leftsum+=nums[i]
        return -1