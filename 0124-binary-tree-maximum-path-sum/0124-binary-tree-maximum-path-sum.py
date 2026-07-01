# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max with split
            result[0] = max(result[0], root.val+leftMax+rightMax)
            # compute max without split
            return root.val + max(leftMax, rightMax)
        
        dfs(root)

        return result[0]

        
