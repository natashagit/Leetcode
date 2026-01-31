class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # first detect cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Detect start of cycle for repeated number
        pointer = 0
        while True:
            pointer = nums[pointer]
            slow = nums[slow]
            if slow == pointer:
                return slow
        