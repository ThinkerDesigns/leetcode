# Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        freq = []
        current = head
        while current:
                freq.append(current.val)
                current = current.next
        print(freq)
        if len(freq) == 1:
            return True
        left = 0
        right = len(freq) - 1
        while left <= right:
            if freq[left] != freq[right]:
                return False
            left += 1
            right -= 1
        return True
