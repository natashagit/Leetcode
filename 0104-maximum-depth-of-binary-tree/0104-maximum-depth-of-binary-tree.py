# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # input: root of binary tree
        # output: max depth of longest path in tree
        # Recursive DFS
        # if root is None:
        #     return 0
    
        # return 1+max(findMaxDepth(root.left), findMaxDepth(root.right))
        
        # Iterative DFS
        # keep a stack to store node and depth
        # keep popping from the stack
        # if node exists
        # update max depth
        
        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                maxDepth = max(maxDepth, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
            
        return maxDepth


