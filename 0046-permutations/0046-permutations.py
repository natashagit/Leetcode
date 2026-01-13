class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # input: nums list
        # output: return list of lists of permutations of nums
        # use result and path to store 
        # keep a boolean for all elements - false initially
        # backtrack by adding one element at a time
        # base case - if the length of path is same as nums - permutation found : append the path to result and return
        # loop through nums and check if used by checking boolean
        # if not used then use element and append to path
        # pop it from path so it can backtrack
        # return result in the end

        result = []
        path = []
        used = [False]*len(nums)
        def backtrack():
            if len(path)==len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]= True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i]=False

        backtrack()
        return result

