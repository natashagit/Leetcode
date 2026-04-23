class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # |-----|
        # |--||--||--|
        # 1--2--3--4
        # [[1,2],[2,3],[3,4],[1,3]]
        # sort
        # [[1,2],[1,3],[2,3],[3,4]]
        intervals = sorted(intervals, key=lambda x:x[1])
        check = intervals[0]
        i = 1
        remove = 0
        while i<len(intervals):
            if intervals[i][0]<check[1]:
                remove+=1
            else:
                check = intervals[i]
            i+=1
        return remove
