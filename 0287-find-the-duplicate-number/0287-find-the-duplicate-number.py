class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums array
        # output: repeated value
        # sorting would make it O(nlogn) time but modify array
        # using set would make it O(n) time and space
        # need to keep at O(1) space
        # if I treat each index as a node and check the next as the nums[index]
        # it would loop withing 1..n
        # would revisit one again as its repeated - forming a cycle
        # the entry point of the cycle is the duplicate value

        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        start = 0
        while True:
            start = nums[start]
            slow = nums[slow]
            if slow==start:
                return slow


        