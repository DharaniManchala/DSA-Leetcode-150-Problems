# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()          # Dummy node to start the merged list
        current = dummy             # Pointer to build the result list
        
        # Loop until either list1 or list2 becomes None
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next   # Move list1 forward
            else:
                current.next = list2
                list2 = list2.next   # Move list2 forward
            current = current.next   # Move the pointer for the result list
        
        # Attach remaining nodes of list1 or list2 (only one of them will be non-null)
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next           # Return head of merged list (skipping dummy)
# Example usage:
# Creating linked lists for testing
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node4 = ListNode(1)
# node5 = ListNode(3)
# node6 = ListNode(4)
# node4.next = node5
# node5.next = node6
# solution = Solution()
# result = solution.mergeTwoLists(node1, node4)
# # Printing the result
# while result:
#     print(result.val, end=" -> ")#     result = result.next
# # This code defines a ListNode class for linked list nodes
# time complexity: O(m + n) where m and n are the lengths of the two linked lists.
# space complexity: O(1) since we are using a constant amount of extra space for