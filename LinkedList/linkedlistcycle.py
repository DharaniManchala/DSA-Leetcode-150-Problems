# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
# Example usage:
# Creating a linked list for testing
# node1 = ListNode(3)
# node2 = ListNode(2)
# node3 = ListNode(0)
# node4 = ListNode(-4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2  # Creating a cycle for testing
# solution = Solution()
# result = solution.hasCycle(node1)
# print(result)  # Should print True if there is a cycle, False otherwise
# time complexity: O(n), where n is the number of nodes in the linked list.
# space complexity: O(1), since we are using a constant amount of extra space for the slow and fast pointers.
# This code defines a ListNode class for linked list nodes and a Solution class with a method
        