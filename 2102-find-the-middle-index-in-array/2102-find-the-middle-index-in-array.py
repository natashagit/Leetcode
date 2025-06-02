class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightcumsum = []
        leftcumsum = []
        flag = False
        for i in range(len(nums)):
            rightcumsum.append(sum(nums)-sum(nums[:i]))
            leftcumsum.append(sum(nums)-sum(nums[i+1:]))
        for j in range(len(rightcumsum)):
            if rightcumsum[j]==leftcumsum[j]:
                flag = True
                break
        if flag==False:
            return -1
        return j