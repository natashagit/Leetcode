class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Add the new interval in
        intervals.append(newInterval)
        # Sort the intervals by first element
        intervals = sorted(intervals, key=lambda x:x[0])
        # Take first interval for comparison
        pair = intervals[0]
        i=1
        result = []
        # Iterate through intervals from second
        while i<len(intervals):
            # If the interval is overlapping, take min and max to merge and update pair
            if pair[1]>=intervals[i][0]:
                pair[0] = min(pair[0], intervals[i][0])
                pair[1] = max(pair[1], intervals[i][1])
            else:
                # No overlap, just append pair to result and update pair to next element
                result.append(pair)
                pair = intervals[i]
            i+=1
        # Append last element in pair
        result.append(pair)
        return result
