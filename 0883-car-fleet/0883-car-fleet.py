class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort in reverse order to loop through from last position to start
        cars = sorted(zip(position, speed), reverse=True)
        
        #Stack to keep track of time of different fleets
        stack = []
        # Loop through and calculate time for each
        for p, s in cars:
            # Calculating time for car
            time = (target - p) / s
            # If stack initially empty, or speed of car closer to target is more than speed of other car
            if not stack or stack[-1]<time:
                # new fleet
                stack.append(time)
        # Total number of fleets
        return len(stack) 
