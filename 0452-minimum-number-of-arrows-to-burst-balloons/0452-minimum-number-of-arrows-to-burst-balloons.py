class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sorted all intervals
        points.sort()
        # Count of balloons to be decremented
        count = len(points)
        # First balloon
        prev = points[0]
        for i in range(1, len(points)):
            # Second balloon onwards
            curr = points[i]
            # If the balloon is overlapping with previous one, one arrow lesser can be used- since one for two
            if curr[0]<=prev[1]:
                count-=1
                # Merging overlapped balloons
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                # Move ahead
                prev = curr

        return count
                

