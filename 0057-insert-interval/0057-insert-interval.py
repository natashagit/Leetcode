class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Since intervals already in ascending, check if second element is smaller than new interval first element
        i=0
        result=[]
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            # Left side elements
            result.append(intervals[i])
            i+=1
        
        # New interval for overlapping range
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        result.append(newInterval)

        #For right side elements
        while i<len(intervals):
            result.append(intervals[i])
            i+=1
        
        return result