# Definition for a Node.
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Clone each node and insert it next to the original
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate original and copied list
        original = head
        copy = head.next
        new_head = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return new_head
# Example usage:
# Creating a linked list with random pointers for testing
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3
# node1.random = node3  # 1's random points to 3
# node2.random = node1  # 2's random points to 1
# node3.random = None    # 3's random points to None
# solution = Solution()
# copied_list = solution.copyRandomList(node1)
# # Printing the copied list
# current = copied_list
# while current:
#     print(f"Node val: {current.val}, Random val: {current.random.val
# if current.random else None}")
#     current = current.next
# time complexity: O(n), where n is the number of nodes in the linked list.
# space complexity: O(n), for the new nodes created in the copied list.
