class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set()
        result = []
        nums_dict = {}
        for num in nums:
            if num in nums_set:
                result.append(num)
            nums_set.add(num)
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                result.append(i)
                break
        return result