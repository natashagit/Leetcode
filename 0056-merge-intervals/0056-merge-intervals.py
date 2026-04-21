class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x:x[0])
        prev = intervals[0]
        i = 1
        result = []
        while i<len(intervals):
            next_start, next_end = intervals[i][0], intervals[i][1]
            prev_start, prev_end = prev[0], prev[1]
            if next_start<=prev_end:
                prev = [prev_start, max(prev_end, next_end)]
            else:
                result.append(prev)
                prev = intervals[i]
            i+=1
        result.append(prev)
        return result
            