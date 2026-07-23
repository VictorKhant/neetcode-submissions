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
            mergeList = []
            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergeList.append(self.merge2Lists(lst1, lst2))
            lists = mergeList
        return lists[0]
    def merge2Lists(self, lst1, lst2):
        tail = dummy = ListNode()
        while lst1 and lst2:
            if lst1.val > lst2.val:
                tail.next = lst2
                lst2 = lst2.next
            else:
                tail.next = lst1
                lst1 = lst1.next
            tail = tail.next
        
        if lst1:
            tail.next = lst1
        else:
            tail.next = lst2
        return dummy.next
