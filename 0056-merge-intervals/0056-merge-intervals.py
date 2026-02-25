class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # input: intervals [[a,b], [c,d]]
        # output: merged intervals [[a,d]]
        # O(nlogn)
        # if no intervals, return []
        # set merged=[]
        # sort all intervals by start time
        # add first interval to merged
        # loop through intervals from 2nd onwards
        # now check if end of interval in merged>=end of current interval
        # if yes-> overlaps: update end of interval in merged with max value of end
        # if no-> add current interval to merged
        # return merged
        merged = []
        intervals.sort(key=lambda x:x[0])
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            last_start, last_end = merged[-1][0], merged[-1][1]
            if last_end>=start:
                merged[-1][1]=max(end, last_end)
            else:
                merged.append(intervals[i])
        return merged
