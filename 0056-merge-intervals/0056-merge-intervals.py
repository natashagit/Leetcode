class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 1
        # First gonna sort the intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        pair = intervals[0]
        while i<len(intervals):
            if pair[1]>=intervals[i][0]:
                pair[1] = max(pair[1], intervals[i][1])
            else:
                result.append(pair)
                pair = intervals[i]
            i+=1
        result.append(pair)
        return result


