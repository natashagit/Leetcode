class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array
        nums = sorted(nums)
        result = []
        # Start by fixing a and having a left and right pointer
        for i in range(len(nums)):
            a = nums[i]
            # Make sure that there are no duplicates
            if i>0 and a==nums[i-1]:
                continue
            # Initialize left and right pointers
            left = i+1
            right = len(nums)-1
            # Check 3sum, move pointers accordingly
            while left<right:
                if nums[left]+nums[right]+a>0:
                    right-=1
                elif nums[left]+nums[right]+a<0:
                    left+=1
                else:
                    result.append([nums[left], nums[right], a])
                    left+=1
                    # check that the next left pointer is not same as previous
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return result


