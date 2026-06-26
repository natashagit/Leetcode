class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: array of numbers, target
        # output: indices of the two numbers that sum up to the target
        # ascending order
        # size of the array?
        # empty array -> []
        # [1] -> []
        # negative numbers
        # Brute force
        # check for every element - O(n^2)
        # Optimal 
        # left and right pointer
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                return [left+1, right+1]
        return []