class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums array
        # output: number of unique elements, list with unique elements
        # two pointers

        # pointer i at 0 and pointer j at 1
        # move pointer i ahead only if vlue of pointer j is different, then set value of new pointer i as value of pointer j and move j ahead
        # return i 

        i = 0
        j = 1
        while j<len(nums):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1