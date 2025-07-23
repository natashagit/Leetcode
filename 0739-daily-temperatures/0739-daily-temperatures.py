class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array for storing index/number of days
        result = [0]*len(temperatures)
        i = 0
        stack = [] # to store temperature and index [t,i]

        for i,t in enumerate(temperatures):
            # if next temperature greater, then pop previous
            while stack and t>stack[-1][0]:
                # if next temperature is greater, pop previous one
                stackt, stacki = stack.pop()
                # store the number of days between previous and new in result
                result[stacki] = i - stacki
            # if next temperature smaller, keep appending to stack
            stack.append([t,i])
        return result