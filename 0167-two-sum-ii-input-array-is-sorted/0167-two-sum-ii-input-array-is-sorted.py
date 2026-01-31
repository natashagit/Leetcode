class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: sorted numbers array, target sum
        # output: return [index1+1, index2+1] of values adding up to target
        # binary search
        # two ptrs, from start and end
        # while start<end
        # if sum of the two > target-> reduce end
        # else increment start
        # else return [start+1, end+1]
        start = 0
        end = len(numbers)-1
        while start<end:
            if numbers[start]+numbers[end]>target:
                end-=1
            elif numbers[start]+numbers[end]<target:
                start+=1
            else:
                return [start+1, end+1]
        return []