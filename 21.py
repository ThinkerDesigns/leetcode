# Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(None)
        result = tmp
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        one = list1
        two = list2
        while one and two:
            if one.val > two.val:
                tmp.next = two
                two = two.next
            elif two.val > one.val:
                tmp.next = one
                one = one.next
            elif two.val == one.val:
                tmp.next = one
                one = one.next
            tmp = tmp.next
        if one:
            tmp.next = one
        elif two:
            tmp.next = two
        return result.next
