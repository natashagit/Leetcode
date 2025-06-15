class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for i in range(len(nums)):
            dict_[nums[i]]=1+dict_.get(nums[i], 0)
            if dict_[nums[i]]>1:
                return True
        return False