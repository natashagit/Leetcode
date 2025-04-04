class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0 
        result = []
        # Left side elements
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1
        # New interval for overlapping one
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        result.append(newInterval)
        # Right side elements
        while i<len(intervals):
            result.append(intervals[i])
            i+=1
        return result