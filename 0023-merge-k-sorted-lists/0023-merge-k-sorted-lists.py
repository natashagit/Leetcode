# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # brute force - use array- sort it and then build ll: O(nlogn)
        def mergeTwo(list1, list2):
            dummy = ListNode(0)
            curr = dummy
            while list1 and list2:
                if list1.val<list2.val:
                    curr.next=list1
                    list1 = list1.next
                else:
                    curr.next=list2
                    list2 = list2.next
                
                curr= curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2

            return dummy.next
        merged = None
        for l in lists:
            merged = mergeTwo(merged, l)
        return merged
        