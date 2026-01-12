class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # A B - A B - A B
        # A B - - A B - - A B
        # A B A B C D 
        # input: tasks list, n for intervals max for same label
        # output: total of time interval
        # maxheap to store max frequency of tasks
        # queue to save the reduced frequency after task done and current time interval + n, so that it can be pushed back into heap at that time
        from collections import Counter, deque
        heap = [-x for x in Counter(tasks).values()]
        heapq.heapify(heap)
        q = deque()
        total_time = 0
        while len(heap)>0 or q:
            total_time+=1
            if heap:
                max_freq = heapq.heappop(heap)
                max_freq+=1
                if max_freq!=0:
                    q.append([max_freq, total_time+n])
            if q and q[0][1]==total_time:
                    temp_freq, time = q.popleft()
                    heapq.heappush(heap, temp_freq)
        return total_time
                

