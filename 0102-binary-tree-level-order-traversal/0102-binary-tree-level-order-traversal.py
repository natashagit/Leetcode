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
        # Breadth First Search
        if root is None:
            return []
        from collections import deque
        q = deque()
        result = []

        q.append(root)
        level = 0

        while q:
            result.append([])
            for _ in range(len(q)):
                node = q.popleft()
                result[level].append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level+=1
        return result