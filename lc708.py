"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            linked = Node(insertVal)
            linked.next = linked
            return linked

        if head.next == head:
            new_node = Node(insertVal)
            head.next = new_node
            new_node.next = head
            return head
        
        prev = head
        current = head.next
        insert_node = Node(insertVal)

        while True:
            if prev.val <= insertVal <= current.val:
                prev.next = insert_node
                insert_node.next = current
                return head

            if (insertVal <= current.val < prev.val) or (current.val < prev.val <= insertVal):
                prev.next = insert_node
                insert_node.next = current
                return head

            prev = current
            current = current.next

            if prev == head:
                break
        
        prev.next = insert_node
        insert_node.next = current

        return head
