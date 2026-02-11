class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # input: nums
        # output: triplets that sum up to 0
        # nums = sorted(nums) nlogn
        # result = []
        # [-4, -1, -1, 0, 1,2]
        # i from 0 to nums len, j at i+1 till j<k, k at end
        # check that nums[i]!=nums[i-1] 
        # check if nums[j]+nums[i]+nums[k]==0
        # if yes, then append triplet to result
        # now increase j and check nums[j]!=nums[j-1] and j<k for duplicates
        # if nums[j]+nums[i]+nums[k]>0-> k reduce
        # if nums[j]+nums[i]+nums[k]<0-> j increase
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k = len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return result