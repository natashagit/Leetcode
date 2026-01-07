# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # input: tree
        # output: level order traversal: level by level in list
        # BFS
        result = []
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if res:
                result.append(res)
        return result
