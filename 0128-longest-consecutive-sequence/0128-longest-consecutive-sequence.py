class Solution(object):
    # input: unsorted array nums
    # output: length of longest consecutive sequence of elements in nums
    # make a set of nums->nums_set
    # loop through nums
    # if element-1 not in nums_set->count=1
        # current=element
        # while current+1 in nums_set
            # count+=1
            # current+=1
        # longest = max(count, longest)

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0
        for i in nums_set:
            if i-1 not in nums_set:
                current = i
                count=1
                while current+1 in nums_set:
                    current+=1
                    count+=1
                longest = max(longest, count)
        return longest