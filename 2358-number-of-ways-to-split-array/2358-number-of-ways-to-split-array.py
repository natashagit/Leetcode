class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftsum = 0 
        splits = 0
        n= len(nums)
        total = sum(nums) 
        # Can only split till before last element
        for i in range(n-1):
            # Adding each element
            leftsum+=nums[i]
            # Remove left sum from total for getting right side sum
            rightsum = total-leftsum
            if leftsum>=rightsum:
                splits+=1
        return splits