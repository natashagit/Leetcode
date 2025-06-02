class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = [1]*len(nums)
        rightproduct = [1]*len(nums)
        final = []
        # Take product of all elements to the left
        for i in range(1, len(nums)):
            leftproduct[i] = nums[i-1]*leftproduct[i-1]
        # Take product of all elements to the right
        for i in range(len(nums)-2, -1, -1):
            rightproduct[i] = nums[i+1]*rightproduct[i+1]
        # Take pairwise product of both
        for i in range(len(nums)):
            final.append(leftproduct[i]*rightproduct[i])

        return final
