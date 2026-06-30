# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # BST: left elements less than node val, right elements> node val
        # If we do normal left and right subtree check, we may miss out on situations where right subtree's left element less than node
        # Brute force approach
        # Need to check if everything on left of node smaller and vice versa
        # DFS for every node -> O(n^2)
        # Optimal approach
        # we can set valid ranges for each node to check their value based on the parent and if its left or right node
        # root -> -infinity to infinity
        # root.left -> -infinity to root.val
        # root.right -> root.val to infinity
        # Complexity: O(n)
        # create a function to check value of node with boundaries recursively
        # check if the node's value not between the boundaries -> return false
        # recursively call the function on node's left and node's right values
        # call the function with initial boundaries on node
        
        def valid_node(node, low, high):
            if node is None:
                return True

            if not (low<node.val<high):
                return False
                
            return valid_node(node.left, low, node.val) and valid_node(node.right, node.val, high)

        return valid_node(root, float("-inf"), float("inf"))
