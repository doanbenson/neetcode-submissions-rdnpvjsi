# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        fast = head
        while fast:
            length += 1
            fast = fast.next
        
        end_index = length - n
        if end_index == 0:
            return head.next

        curr = head
        i = 0
        while curr and i < end_index:
            if (i + 1) == end_index:
                curr.next = curr.next.next
                break
            curr = curr.next
            i += 1

        return head


            