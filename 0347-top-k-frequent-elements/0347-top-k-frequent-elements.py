class Solution(object):
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # input: array of numbers, integer k
        # output: top k frequent numbers in the array
        # k always valid, 1<=k<number of unique elements
        # same frequency, then order doesn't matter
        # result not in particular order
        # brute force
        # add values into dict with count and sort by values in descending order and take the first k elements
        # O(nlogn)
        # optimal approach
        # keep a hashmap for frequency of each element
        # as max frequency of any number is size of nums, size of array -> size of nums
        # make buckets where index shows frequency
        # add values into the array if it is of that frequency
        # return those values in descending order
        # O(n)

        from collections import Counter

        count = Counter(nums) # {1:3, 2:2, 3:1}

        arr = [[] for _ in range(len(nums)+1)]
        for key,value in count.items():
            arr[value].append(key)
        # [[], [3], [2], [1], [], []]
        result = []

        for i in range(len(arr)-1, 0, -1):
            for key in arr[i]:
                result.append(key)
                if len(result)==k:
                    return result

        




