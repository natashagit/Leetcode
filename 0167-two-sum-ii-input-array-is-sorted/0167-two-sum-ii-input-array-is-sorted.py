class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while(start<end):
            if (numbers[start]+numbers[end])>target:
                end-=1
            elif (numbers[start]+numbers[end])<target:
                start+=1
            else:
                break
        return [start+1, end+1]