# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
    
        parent = {}

        def dfs(node, par = None):
            if not node:
                return 
            
            parent[node]=par
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)

        from collections import deque
        q = deque()
        q.append((target, 0)) #node and distance

        visited = set()
        visited.add(target)
        result = []
        while q:
            new_node, distance = q.popleft()

            if distance==k:
                result.append(new_node.val)
            
            if distance>k:
                break
            

            neighbors = [new_node.left, new_node.right, parent[new_node]]

            for nei in neighbors:
                if nei and nei not in visited:
                    visited.add(nei)
                    q.append((nei, distance+1))
            
        return result



