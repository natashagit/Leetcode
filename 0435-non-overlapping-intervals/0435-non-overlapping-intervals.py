class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        pair = intervals[0]
        result = 0
        for i in range(1, len(intervals)):
            # overlaps
            if intervals[i][0]<pair[1]:
                result+=1
                pair[1]=min(intervals[i][1], pair[1])
            else:
                pair = intervals[i]
        return result

                