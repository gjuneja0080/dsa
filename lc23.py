# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return
        def merge(list1, list2):
            if not list1: return list2
            res = ListNode()
            dummy = res
            while list1 and list2:
                if list1.val <= list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next
            if list1:
                dummy.next = list1
            if list2:
                dummy.next = list2
            return res.next

        ans = []
        for i in range(len(lists)):
            ans = merge(ans, lists[i])
        return ans
