class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # input: list of elements
        # output: next permutation list in lexicographical order 
        # brute:
        # generate all permutations using recursion
        # do linear search and get next permutation
        # it will take O(n! X n), too long - need to optimize

        # Optimal soln:
        # from the end of the array check backwards for where nums[i]<nums[i+1] and store index
        # check index exists, if no such value where nums[i]<nums[i+1]-> reverse the array and return for next permutation
        # run backwards from end of nums to index
        # if nums[i]>nums[index]
        # swap nums[i] with nums[index] to get next biggest permutation
        # reverse the remaining array to make it as small as possible

        ind = -1
        n = len(nums)
        # [3,2,1]
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        if ind==-1:
            nums.reverse()
            return nums
        
        for i in range(n-1, ind, -1):
            if nums[i]>nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        temp = nums[ind+1:]
        temp.reverse()
        nums[ind+1:] = temp
        return nums

