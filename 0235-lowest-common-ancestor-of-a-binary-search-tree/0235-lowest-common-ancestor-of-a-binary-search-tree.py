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
        # input: tree
        # output: LCA - can be parent of both if common, or if one is parent of other
        # p>root and q>root -> move right recursively;
        # p<root and q<root -> move left;
        # else -> root is LCA

        if root is None:
            return 
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root