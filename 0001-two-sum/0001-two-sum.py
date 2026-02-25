class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: array nums, target integer
        # output: indices of the two numbers-> target
        # negatives and duplicates
        # constraints on input nums size -> 10^4 : less than O(n^2)
        # naive approach: check every pair (i, j) O(n^2)
        # optimized approach: hashmap to store the number, index; For each number, we want to know if we’ve already seen target - number
        # keep hashmap seen
        # for each index i in nums
        # need = target - nums[i]
        # if need is in seen: return seen[need], i
        # avoids using same element twice

        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [i, seen[need]]
            seen[nums[i]] = i
        return []

        

    





    