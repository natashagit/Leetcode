# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # If either are empty return None
        if not postorder or not inorder:
            return None
        
        # Last element in postorder is root, popped
        root = TreeNode(postorder.pop())
        # The root is the middle element in inorder
        mid = inorder.index(root.val)
        # Right element of root are the values to right of mid in inorder
        root.right = self.buildTree(inorder[mid+1:], postorder)
        # Left element of root are the values to left of mid in inorder
        root.left = self.buildTree(inorder[:mid], postorder)
        return root


        