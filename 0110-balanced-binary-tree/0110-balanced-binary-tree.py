# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # input: tree 
        # output: true if difference between height of left and right subtree of every node is <=1 - balanced tree
        # O(n^2) solution
        # check at every node height
        # compute the difference btwn heights of left and right subtrees
        # if difference>1 - return False
        
        # O(n) solution
        # do a dfs by finding left height and right height
        # return -1 if the difference between the two is >1
        # if heights are -1 then return -1
        # return the max height
        # if the height returned is not -1 return True, else False
        
        def dfs(root):
            if root is None:
                return 0
            left_height = dfs(root.left)
            if left_height==-1:
                return -1
            right_height = dfs(root.right)
            if right_height==-1:
                return -1
            if abs(left_height-right_height)>1:
                return -1
            
            return 1+max(left_height, right_height)
        
        if dfs(root)==-1:
            return False
        else:
            return True