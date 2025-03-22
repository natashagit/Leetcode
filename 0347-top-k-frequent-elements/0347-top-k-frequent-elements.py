class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time Complexity: O(nlogk)
        # Using min heap
        import heapq # min-heap library
        from collections import Counter
        counter = Counter(nums) # creates a dictionary in O(n) with freq
        heap = []
        # Push all values with freq onto min heap
        # Push new val with freq and Pop the value with minimum freq from top of heap until the heap has k elements and then return heap containing k most freq elements
        for key, val in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(val, key))
            else:
                heapq.heappushpop(heap, (val,key))
        return [h[1] for h in heap]
            
        # Time Complexity: O(nlogn)
        # Create a dict with count for each element in the array
        dic = {}
        result = []
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        # Create empty array and append values in position of count
        freq = [[] for i in range(len(nums)+1)]
        for n, count in dic.items():
            freq[count].append(n)
        
        for i in range(len(freq)-1, 0 ,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result

        
        


