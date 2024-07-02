# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(list1, list2):
            if not list1: return list2
            if not list2: return list1

            if list1.val <= list2.val:
                list1.next = merge(list1.next, list2)
                return list1
            else:
                list2.next = merge(list1, list2.next)
                return list2
        
        def get_midpoint(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        if not head or not head.next: return head
        first_half = head
        second_half = get_midpoint(first_half)
        temp = second_half.next
        second_half.next = None
        second_half = temp

        left = self.sortList(first_half)
        right = self.sortList(second_half)

        return merge(left, right)

