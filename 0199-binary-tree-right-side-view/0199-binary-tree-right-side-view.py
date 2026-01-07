# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # input: tree
        # output: right side view nodes
        # BFS level order - take nodes on right only, if right not there then take left
        from collections import deque
        q = deque()
        q.append(root)
        result = []
        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if res:
                result.append(res[-1])
        return result