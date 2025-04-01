# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        A = []
        def InOrder(node):
            if node is None:
                return
            InOrder(node.left)
            A.append(node.val)
            InOrder(node.right)
        InOrder(root)
        return A[k-1]