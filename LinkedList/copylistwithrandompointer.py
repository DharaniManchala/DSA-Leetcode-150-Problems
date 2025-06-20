"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        current=head
        while current:
            newnode=Node(current.val)
            newnode.next=current.next
            current.next=newnode
            current=newnode.next
        current=head
        while current:
            if current.random:
                current.next.random=current.random.next
            current=current.next.next
        original=head
        copy=head.next
        newhead=copy
        while original:
            original.next=original.next.next
            if copy.next:
                copy.next=copy.next.next
            original=original.next
            copy=copy.next
        return newhead
            

# Example usage:
# Creating a linked list for testing
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3
# node1.random = node3  # 1's random points to 3
# node2.random = node1  # 2's random points to 1
# solution = Solution()
# result = solution.copyRandomList(node1)
# # Printing the result
# current = result
# while current:
#     print(f"Node val: {current.val}, Random val: {current.random.val if current.random else None}")
#     current = current.next
# time complexity: O(n), where n is the number of nodes in the linked list.
# space complexity: O(n), since we are creating a new linked list with the same number
