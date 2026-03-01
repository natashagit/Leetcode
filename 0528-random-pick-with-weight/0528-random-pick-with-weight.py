class Solution(object):
# build prefix sum array
# generate random number
# use binary search to find where the number falls
    def __init__(self, w):
        """
        :type w: List[int]
        """
        # to pick an index with probability sum(w) till w
        self.ranges = []
        total = 0
        for weight in w:
            total+=weight
            self.ranges.append(total)
        self.total = total    
        

    def pickIndex(self):
        """
        :rtype: int
        """
        # generating a random number between the total range
        rand_num = random.randint(0, self.total-1)
        left, right = 0, len(self.ranges)-1
        while left<right:
            mid = (left+right)//2
            if rand_num>=self.ranges[mid]:
                left = mid+1
            else:
                right = mid
        return right
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()