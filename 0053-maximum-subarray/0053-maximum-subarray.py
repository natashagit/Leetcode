class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = max(nums)
        currSum = 0
        for n in nums:
            if currSum<0:
                currSum = 0
            currSum+=n
            maxSub = max(maxSub, currSum)

        return maxSub