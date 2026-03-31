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
        # output: sorted list 
        dummy = ListNode()
        head = dummy
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 and list2:
            if list1.val<list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next
        while list1:
            dummy.next = ListNode(list1.val)
            dummy = dummy.next
            list1 = list1.next
        while list2:
            dummy.next = ListNode(list2.val)
            dummy = dummy.next
            list2 = list2.next
        return head.next
