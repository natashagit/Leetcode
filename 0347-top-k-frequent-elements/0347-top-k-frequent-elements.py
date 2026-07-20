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
        freq = Counter(nums)

        max_heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(max_heap)

        result = []
        for _ in range(k):
            count, num = heapq.heappop(max_heap)
            result.append(num)
        return result

        




