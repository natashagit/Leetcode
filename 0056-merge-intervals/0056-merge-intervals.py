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
        # Take first interval for comparison 
        pair = intervals[0]
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


