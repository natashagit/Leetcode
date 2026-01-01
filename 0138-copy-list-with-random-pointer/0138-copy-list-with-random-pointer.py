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
        # input: ll with random ptr
        # output: deep copy of the ll including the random ptr
        # edge case: empty list

        # hashmap to store the ll
        # create copies of nodes and store into hashmap old Node:new Node
        # assign next and random ptrs by mapping the each copy to the next and random ptr
        # return the new copy of head

        copymap = {None: None}

        old = head
        while old:
            copymap[old] = Node(old.val)
            old = old.next
        
        curr = head
        while curr:
            copymap[curr].next = copymap[curr.next]
            copymap[curr].random = copymap[curr.random]
            curr = curr.next
        
        return copymap[head]
        