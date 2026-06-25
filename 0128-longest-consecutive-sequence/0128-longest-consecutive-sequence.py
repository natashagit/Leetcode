class Solution(object):
    
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: list of numbers
        # output: length of longest list containing consecutive numbers
        # no consecutive elements - return 0
        # values negative - yes
        # duplicates - yes
        # empty array - return 0
        # size of array 
        # edge cases: [], [1], 
        # brute force
        # loop through nums, while n+1 present->update length and keep max length
        # checking existence n times for n numbers
        # O(n^2)
        # Better approach
        # Sorting it: [1,2,3,4,100,200] 
        # can see consecutive number by next
        # O(nlogn)
        # Optimal approach
        # make a set of array
        # for value in array check if value-1 in array-> if not, then start and check value+1 onwards and increase length 

        maxlength = 0
        length = 0
        arr_set = set(nums) #{100,4,200,1,3,2}
        for num in arr_set: 
            if num-1 not in arr_set:
                length = 1
                current = num

                while current+1 in arr_set:
                    current+=1
                    length+=1
            
                maxlength = max(length, maxlength)

        return maxlength
