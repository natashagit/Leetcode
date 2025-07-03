# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Root is first element in preorder
        root = TreeNode(preorder[0])
        # The root is the mid value in inorder
        mid = inorder.index(preorder[0])
        # The left is all the elements to the left of mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # The right is all the elements to the right of mid
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
    
        