class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # To keep track of max and min subarray products in array
        currMax, currMin = 1,1
        # Initally result set to max in array
        result = max(nums)
        # Loop through nums and calculate max and min of product with self
        for n in nums:
            # Storing so can use for currMin
            tmp = n*currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            result = max(result, currMax)
        
        return result
