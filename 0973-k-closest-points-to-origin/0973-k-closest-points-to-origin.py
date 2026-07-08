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
        import heapq, math
        max_heap = []


        for x,y in points:
            distance = math.sqrt(x**2+y**2)
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        
        result = []

        for _, x, y in max_heap:
            result.append([x,y])
    
        return result
