class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # input: nums in rotated but sorted order, target
        # output: index of target value
        # can check if first half or second half sorted
        # search for target in sorted half with binary search
        # if not there then check the unsorted half with binary search
        low = 0
        high = len(nums)-1
        while low<=high:
            mid_pt = (low+high)//2
            if target==nums[mid_pt]:
                return mid_pt
            # first half sorted
            if nums[mid_pt]>=nums[low]:
                if target>=nums[low] and target<nums[mid_pt]:
                    high = mid_pt-1
                else:
                    low = mid_pt+1
            else:
                if target>nums[mid_pt] and target<=nums[high]:
                    low = mid_pt+1
                else:
                    high = mid_pt-1
        return -1

