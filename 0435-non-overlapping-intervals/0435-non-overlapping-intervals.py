class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start value
        intervals.sort()
        end_prev = intervals[0][1]
        result = 0
        # Compare first interval with next to check if overlapping
        for i in range(1, len(intervals)):
            # Check if next interval's start is before prev interval's end
            if intervals[i][0]>=end_prev:
                # No overlapping, so move ahead and keep the next interval's endpoint
                end_prev = intervals[i][1]
            else:
                #overlaps so need to remove 1
                result+=1
                # Update prev interval's end point by continuing with the interval that has a shorter end point
                end_prev = min(end_prev, intervals[i][1])
        return result

                