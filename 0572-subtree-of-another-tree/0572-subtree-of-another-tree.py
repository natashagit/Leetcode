# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # input: tree and subroot
        # output: return false if subroot is in tree
        # check is same tree now for subroot and tree
        # recursively check for left of tree with subroot or right of tree with subroot
        def isSameTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if root is None:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)