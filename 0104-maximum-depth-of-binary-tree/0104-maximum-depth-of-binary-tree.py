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
        # Iterative BFS
        if root == None:
            return 0
        from collections import deque
        q = deque()
        res = []

        q.append(root)
        currLevel = 0

        while q:
            res.append([])
            for _ in range(len(q)):
                node = q.popleft()
                res[currLevel].append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            currLevel+=1
        return currLevel


        # Recursive way
        # if root == None:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return (1+max(left,right))
        
        