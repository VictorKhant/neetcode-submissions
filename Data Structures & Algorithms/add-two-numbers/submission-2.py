# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = temp = ListNode()
        while l1 and l2:
            res = l1.val + l2.val + carry
            temp.next = ListNode(res % 10)
            temp = temp.next
            carry = res // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            res = l1.val + carry
            temp.next = ListNode(res % 10)
            carry = res // 10
            temp = temp.next
            l1 = l1.next
        while l2:
            res = l2.val + carry
            temp.next = ListNode(res % 10)
            carry = res // 10
            temp = temp.next
            l2 = l2.next
        if carry:
            temp.next = ListNode(carry)
        return dummy.next
           


