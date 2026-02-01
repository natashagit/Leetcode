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
        # if yes then increment the counter
        counter = 0
        dict_prefix = {0:1}
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
            

