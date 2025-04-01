# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        curr = root.val
        # If root is greater than p and q, move left
        if curr>p.val and curr>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If root is less than p and q, move right
        if curr<p.val and curr<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Else return root
        return root
