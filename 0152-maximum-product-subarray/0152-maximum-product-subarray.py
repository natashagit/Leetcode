class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity = O(n)
        # Different cases: 
        # 1. All positive = Even -ve, 2. Odd -ve, 3. Zeroes
        # For 2. case -> Can be split on odd -ve
        # For 3. case -> Can be split on zeroes by setting prefix=1
        max_prod = -float("inf")
        prefix = 1
        suffix = 1
        # Looping from start to end and calculating prefix and max 
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            prefix = prefix * nums[i]
            max_prod = max(prefix, max_prod)
        for i in range(len(nums)-1, -1, -1):
            if suffix == 0:
                suffix = 1
            suffix = suffix * nums[i]
            max_prod = max(suffix, max_prod)
        return max_prod

        # Time Complexity = O(n^2)
        # max_prod = -float("inf")
        # prod = 1
        # for i in range(len(nums)):
        #     prod = nums[0]
        #     for j in range(1, len(nums)):
        #         prod = prod * nums[j]
        #         max_prod = max(prod, max_prod)
        # return max_prod