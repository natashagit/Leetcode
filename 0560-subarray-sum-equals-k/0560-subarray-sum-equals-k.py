class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # inputs: list of numbers, value k
        # outputs: number of subarrays that have sum k
        # edge cases: no sum is k, empty array
        # prefix[r]-prefix[l-1]=k then subarray present
        # keep a dict to maintain the prefix sum with count of it
        # add prefix sum to dict
        # check if prefix-k is present in dict
        # if yes then increment the counter with value in dict
        # So every time we reach a prefix sum S, we ask:
        # “How many times have I previously seen S - k?”
    
        # input: nums, k
        # output: total number of subarrays whose sum=k
        # no sum is k, empty array
        # no negative numbers
        # result=0
        # traverse through array and if sum=k -> store count in dict with sum
        # 0:1, 1:1, 2:1, 3:1
        # if sum - k is there in dict -> there is a subarray-> increment and store in result
        summ = 0
        dict_sums = {0:1}
        result = 0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ-k in dict_sums:
                result+=dict_sums[summ-k]
            if summ not in dict_sums:
                dict_sums[summ]=1
            else:
                dict_sums[summ]+=1
        return result
