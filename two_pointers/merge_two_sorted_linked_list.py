# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list2.val < list1.val:
            list1, list2 = list2, list1

        head = list1
        while list1 and list1.next and list2:
            if list1.next.val >= list2.val:
                tmp1, tmp2 = list1.next, list2.next
                list1.next, list2.next = list2, tmp1
                list2 = tmp2
            else:
                list1 = list1.next
        if not list1.next:
            list1.next = list2
        return head
            