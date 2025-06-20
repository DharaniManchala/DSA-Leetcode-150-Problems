# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Step 0: Create a dummy node to simplify edge cases (e.g., left = 1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move `prev` to the node just before the "left" position
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Start reversing the sublist from `left` to `right`
        # `current` points to the node at position "left"
        current = prev.next
        for _ in range(right - left):
            temp = current.next               # Node to move
            current.next = temp.next         # Remove temp from list
            temp.next = prev.next            # Insert temp after prev
            prev.next = temp                 # Connect prev to temp

        return dummy.next  # Return new head
# Example usage:
# Creating a linked list for testing
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# solution = Solution()
# result = solution.reverseBetween(node1, 2, 4)
# # Printing the result
# current = result
# while current:
#     print(current.val, end=" -> ")#     current = current.next
# # This code defines a ListNode class for linked list nodes
# time complexity: O(n), where n is the number of nodes in the linked list.
# space complexity: O(1), since we are using a constant amount of extra space for