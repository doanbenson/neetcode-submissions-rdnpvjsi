# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_list.append(self.mergeLists(list1, list2))
            lists = merged_list
        
        return lists[0]

    def mergeLists(self, list1, list2):
        builder = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                builder.next = list1
                list1 = list1.next
            else:
                builder.next = list2
                list2 = list2.next
            builder = builder.next
        
        if list1:
            builder.next = list1
        if list2:
            builder.next = list2
        
        return dummy.next
