# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if not head or not head.next: return head
            left, right = None, head

            while right:
                tmp, right.next = right.next, left
                left, right = right, tmp

            return left
    
    def isEqual(self, one, two):
        while one and two:
            if one.val != two.val: return False
            one = one.next
            two = two.next
        return True
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        slow = self.reverse(slow)
        
        return self.isEqual(head, slow)
            