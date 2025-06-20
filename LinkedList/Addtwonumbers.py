# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current=dummy
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            total=val1+val2+carry
            carry=total//10
            current.next=ListNode(total%10)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
# Example usage:
# Creating linked lists for testing
# node1 = ListNode(2)
# node2 = ListNode(4)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3
# node4 = ListNode(5)
# node5 = ListNode(6)
# node6 = ListNode(4)
# node4.next = node5
# node5.next = node6
# solution = Solution()
# result = solution.addTwoNumbers(node1, node4)
# # Printing the result
# current = result
# while current:
#     print(current.val, end=" -> ")
#     current = current.next
# # This code defines a ListNode class for linked list nodes
# time complexity: O(max(m, n)), where m and n are the lengths of the two linked lists.
# space complexity: O(max(m, n)), since we are creating a new linked list to
    