class MedianFinder(object):

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # add to left heap which is a max heap
        heapq.heappush(self.left, -num)

        # right heap always has values>left heap
        # push largest of left heap to right heap to keep that order
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # if right has more elements move smallest back to left
        if len(self.right)>len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left)>len(self.right):
            return float(-self.left[0])
        return (-self.left[0]+self.right[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()