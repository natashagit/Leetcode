class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, startTime: int, endTime: int) -> bool:
        #If new interval overlaps with overlapping ones - triple booking - set False
        for start, end in self.overlapping:
            if endTime>start and startTime<end:
                return False
        
        #If new interval overlaps with non_overlapping one - save overlapping region - set True
        for start, end in self.non_overlapping:
            if endTime>start and startTime<end:
                self.overlapping.append((max(start,startTime), min(end, endTime)))
        #Save new interval in non_overlapping
        self.non_overlapping.append((startTime, endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)