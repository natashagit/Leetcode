# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Use recursive fn to check
        def valid(node, left, right):
            # If empty, return true    
            if not node:
                return True
            # If out of bounds, return false
            if not(node.val<right and node.val>left):
                return False
            # If it goes left or right, bounds accordingly set
            return (valid(node.left, left, node.val) and (valid(node.right, node.val, right)))
        # Pass the initial root and bounds to recursively check
        return valid(root, float("-inf"), float("inf"))
        