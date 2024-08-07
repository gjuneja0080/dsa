# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        current = res
        while l1 or l2 or carry:
            sumval = carry
            if l1:
                sumval += l1.val
                l1 = l1.next
            if l2:
                sumval += l2.val
                l2 = l2.next
            current.next = ListNode(sumval % 10)
            carry = sumval // 10
            current = current.next

        return res.next
