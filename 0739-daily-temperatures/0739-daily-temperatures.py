class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # input: temperatures array
        # output: array consisting of number of days it takes to get warmer from the ith day
        # no elements -> []
        # 1 element -> 0
        # equal?
        # brute force
        # can loop through for every element and check
        # O(n^2)
        # Optimal
        # stack to store indices of days waiting for warmer temp
        # when u find warmer day -> store the current index-stack[-1]
        
        stack = [0]
        answer = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                answer[stack[-1]] = i-stack[-1]
                stack.pop()
            
            stack.append(i)
        return answer
