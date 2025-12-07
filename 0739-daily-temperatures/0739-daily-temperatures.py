class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # input: list of temperatures
        # output: list of number of days to wait for warmer temp

        # stack = []
        # answer = [0]*len(temperatures)
        
        stack = []
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i-prev
            stack.append(i)
        
        return answer
