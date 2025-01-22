class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # jumps straight to element without prev consecutive numbers
            if (num-1) not in numSet:
                length=1
                # if the next consecutive element present
                while (num+length) in numSet:
                    # increase length
                    length+=1
                # calculate the max length of consecutive seq
                longest = max(length, longest)
        return longest