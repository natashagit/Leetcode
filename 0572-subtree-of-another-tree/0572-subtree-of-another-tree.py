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
        # If subtree is null, can still be a subtree
        if not subRoot:
            return True
        # If tree is null, can't have subtree
        if not root:
            return False
        # Check if subtree is the same tree as tree
        if self.sameTree(root, subRoot):
            return True
        # Recursively call isSubtree to check on left and right subtree of tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    # Function created to check if same tree
    def sameTree(self, root, subRoot):
        # If both are empty, return true
        if not subRoot and not root:
            return True
        # If the values are equal in both subtree and tree
        if subRoot and root and subRoot.val == root.val:
            # Recursively call sameTree to check on all left and right nodes to be equal
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        # Else return false
        return False

        