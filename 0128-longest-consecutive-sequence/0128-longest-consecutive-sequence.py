class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # jumps straight to element without prev consecutive numbers
            if (num-1) not in numSet:
                length=0
                # if the next consecutive element present
                while (num+length) in numSet:
                    # increase length
                    length+=1
                # calculate the max length of consecutive seq
                longest = max(length, longest)
        return longest


            
