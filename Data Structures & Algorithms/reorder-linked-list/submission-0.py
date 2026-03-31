# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_section = slow.next
        prev = slow.next = None

        while second_section:
            tmp = second_section.next
            second_section.next = prev
            prev = second_section
            second_section = tmp

        first, second_section = head, prev
        while second_section:
            tmp1, tmp2 = first.next, second_section.next
            first.next = second_section
            second_section.next = tmp1
            first, second_section = tmp1, tmp2

