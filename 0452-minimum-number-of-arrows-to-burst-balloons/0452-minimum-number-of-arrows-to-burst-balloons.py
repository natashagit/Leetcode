class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # input: balloon start and end points in array
        # output: number of minimum arrows to burst all balloons
        # constraints: 10^5 -> O(nlogn) or O(n)
        # edge cases: empty input, one balloon, negative coordinates
        # implement: 
        # sort by end point of balloon diameter
        # [[10,16],[2,8],[1,6],[7,12]]
        # [[1,6], [2,8], [7, 12], [10,16]]
        # shoot the end of earliest balloon
        # if the end>start of next balloon -> gets burst
        # else now the next balloon is shot at new end -> counter increment
        points.sort(key=lambda x: x[1])
        counter = 1
        i = 1
        end = points[0][1]
        counter = 1
        while i<len(points):
            if end<points[i][0]:
                counter+=1
                end = points[i][1]
            i+=1
        return counter


