class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        init = intervals[0]
        i=1
        result = []
        while i<len(intervals):
            # if so then merge and set init
            if intervals[i][0]<=init[1]:
                init[0]=min(init[0], intervals[i][0])
                init[1]=max(init[1], intervals[i][1])
            else:
                result.append(init)
                init = intervals[i]
            
            i+=1
        result.append(init)
        return result

            

            

        

