class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # input: nums array sorted, target
        # output: index of target or else -1
        # negative
        # empty -> -1
        # duplicate values
        # take low and high pts as start and end
        # take mid point and compare with target
        # if mid pt>target: set high to mid pt-1
        # else set low to mid pt+1
        # if mid pt==target: return index

        low = 0
        high = len(nums)-1
        # [5] 5
        while low<=high: # low=0, high=0, mid_pt=3
            mid_pt = (low+high)//2
            if target>nums[mid_pt]:
                low = mid_pt+1
            elif target<nums[mid_pt]:
                high = mid_pt-1
            else:
                return mid_pt
        return -1