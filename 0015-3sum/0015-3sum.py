class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity = O(n^2)
        result = set()
        # Loop through nums with i and j
        for i in range(len(nums)):
            hash_set = set()
            j=i+1
            while j<len(nums):
                # Take sum of ith element and jth element
                sum_ = -(nums[i]+nums[j])
                # If -sum in hashset
                if sum_ in hash_set:
                    # append to result
                    result.add(tuple(sorted([nums[i], nums[j], sum_])))
                # add jth element to hashset and move on
                hash_set.add(nums[j])
                j+=1   
        return [list(triplet) for triplet in result]    
        




        # Time Complexity = O(n^3)
        # result = []
        # # Sort nums
        # nums.sort()

        # # Loop through with i and j from start and k from the end
        # for i in range(len(nums)):
        #     # Check if next element same as previous - ignore for duplicates an continue
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     j = i+1
        #     k = len(nums)-1
        #     while (j<k):
        #         sum_ = nums[i] + nums[j] + nums[k]
        #         if sum_>0:
        #             k-=1
        #         elif sum_<0:
        #             j+=1
        #         else:
        #             result.append([nums[i], nums[j], nums[k]])
        #             j+=1
        #             # Check for duplicate
        #             if j<k and nums[j]==nums[j-1]:
        #                 j+=1
        # return result                              

