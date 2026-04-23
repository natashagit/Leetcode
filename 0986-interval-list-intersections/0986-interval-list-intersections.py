class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        i = j = 0
        output = []
        while i<len(firstList) and j<len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start<=end:
                output.append([start, end])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return output

        