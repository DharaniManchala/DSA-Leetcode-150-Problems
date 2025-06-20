class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next         # move 1 step
        fast = fast.next.next    # move 2 steps
        if slow == fast:
            return True          # cycle detected
    return False                 # no cycle
# Example usage:
# Creating a linked list with a cycle for testing
# node1 = ListNode(3)
# node2 = ListNode(2)
# node3 = ListNode(0)
# node4 = ListNode(-4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2  # Creates a cycle here
# print(hasCycle(node1))  # Should return True if the cycle exists
# Creating a linked list without a cycle for testing
# node1 = ListNode(1)
# node2 = ListNode(2)
# node1.next = node2
# print(hasCycle(node1))  # Should return False if no cycle exists
# This code defines a ListNode class for linked list nodes and a function to detect cycles in a linked list using the Floyd's Tortoise and Hare algorithm.
# The function returns True if a cycle is detected, otherwise it returns False.
# time complexity: O(n), where n is the number of nodes in the linked list
# space complexity: O(1), since we are using only two pointers