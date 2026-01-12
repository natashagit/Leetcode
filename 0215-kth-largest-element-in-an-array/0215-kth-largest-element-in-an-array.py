class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # input: nums, k
        # output: kth largest element
        # minheap -> and pop the top element-> will be the kth largest

        minheap = nums
        heapq.heapify(minheap)
        while len(minheap)>k:
            heapq.heappop(minheap)
        return minheap[0]