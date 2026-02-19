# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # input: list1 and list2
        # output: merged sorted list
        # result -> keep a new ListNode()
        # temp= result
        # loop through while both lists last
        # for every value in list1 and list2 check which is smaller
        # then set the next of temp to the smaller one
        # in end the add all in list1 and list2

        result = ListNode()
        temp = result
        while list1 and list2:
            if list1.val<list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
            
        if list2:
            temp.next = list2
            
        return result.next