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
        counter = 0
        dict_prefix = {0:1} # add count 1 for 0 prefix_sum before array
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum-k in dict_prefix:
                counter+=dict_prefix[prefix_sum-k]
            if prefix_sum in dict_prefix:
                dict_prefix[prefix_sum]+=1
            else:
                dict_prefix[prefix_sum]=1
        return counter
            

