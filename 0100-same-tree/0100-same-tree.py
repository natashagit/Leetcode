# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # If leaves are none
        if p is None or q is None:
            return (p==q)
            
        # Pre-order traversal - Root left right
        return (p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)