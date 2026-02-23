"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # input: linked list with node val, random ptr
        # output: deep copy of the same
        # 2 passes
        # first pass: create copies of nodes as hashmap to new nodes
        # second pass: set random and next pointers 

        copy_list = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copy_list[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copy_list[curr]
            copy.next = copy_list[curr.next]
            copy.random = copy_list[curr.random]
            curr = curr.next
        
        return copy_list[head]
