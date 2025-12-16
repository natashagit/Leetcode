class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: list of 0's and 1's
        # output: length of longest subarray with equal 0's and 1's
        # edge cases: empty list, no equal subarrays

        # [1, 0, 1, 1, 1, 0, 0]
        # {1:0, 0:2, 2:3, 3:4, } 
        # initalize a dict to keep count of sums
        # set length=0
        # loop through list
        # increment sum if 1
        # decrement sum if 0
        # if sum is 0 then length=i+1
        # else if sum in dict-> length = max(length, i-dict[sum])
        # if sum not in dict-> dict[sum]= i

        dict_ = {}
        result = 0
        continuous_sum = 0
            
        for i in range(len(nums)):
            if nums[i]==1:
                continuous_sum+=1
            else:
                continuous_sum-=1
            if continuous_sum==0:
                result = i+1
            elif continuous_sum in dict_:
                result = max(result, i-dict_[continuous_sum])
            else:
                dict_[continuous_sum]=i
        return result
