class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # input: points array with coordinates
        # output: points array with k points that have distances closest to origin
        # kth smallest distances -> maxheap
        heap = []
        for x,y in points:
            d = math.sqrt((x**2)+(y**2))
            heap.append((-d, x, y))
        
        heapq.heapify(heap)
        print(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        
        return [[x,y] for (_, x, y) in heap]
