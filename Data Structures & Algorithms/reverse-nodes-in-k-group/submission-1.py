# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        preGp = dummy
        while True:
            kth = self.getKth(preGp, k)
            if not kth:
                break
            nextGp = kth.next
            prev, curr = kth.next, preGp.next
            while curr != nextGp:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = preGp.next
            preGp.next = kth
            preGp = temp
        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr