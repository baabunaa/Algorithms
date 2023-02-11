# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head

        while head and head.val == val:
            head = head.next
        tmp = head
        while tmp and tmp.next:
            while tmp.next and tmp.next.val == val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head
