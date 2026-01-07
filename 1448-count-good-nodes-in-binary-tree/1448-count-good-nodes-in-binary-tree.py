# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # input: tree
        # output: number of nodes that are good: nodes that are bigger than or equal to parent
        # dfs
        # check that the node value>maxVal-> result=1 else 0, will increment for left nodes and right nodes
        # maxVal is updated by taking max of current node value
        # return result+left good nodes + right good nodes

        def dfs(node, maxVal):
            if node is None:
                return 0

            if node.val>=maxVal:
                result = 1
            else:
                result = 0
            maxVal = max(node.val, maxVal)
            left_good = dfs(node.left, maxVal)
            right_good = dfs(node.right, maxVal)
            return result + left_good + right_good
        return dfs(root, root.val)        

