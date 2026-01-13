class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # input: candidates and target
        # output: combinations of all candidates summing up to target

        candidates.sort()
        result = []
        path = []
        def dfs(i, remaining):
            if remaining==0:
                result.append(path[:])
                return
            for j in range(i, len(candidates)):
                # skip duplicate numbers
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                # don't need to add candidate if more than remaining
                if candidates[j]>remaining:
                    break
                path.append(candidates[j])
                dfs(j+1, remaining-candidates[j])
                path.pop()
        dfs(0, target)
        return result