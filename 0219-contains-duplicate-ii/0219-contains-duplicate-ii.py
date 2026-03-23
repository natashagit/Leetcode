class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # input: nums array, k
        # output: return True if: nums[i]==nums[j] and abs(i-j)<=k
        # empty, one element
        # put values in dict with its index
        # if we come across same number -> check if the curr index- index in dict<=k -> True
        # Update index if we see a same number

        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i-dic[nums[i]]<=k:
                    return True
            dic[nums[i]]=i
        return False
