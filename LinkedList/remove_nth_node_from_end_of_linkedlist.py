class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Step 1: Create a dummy node pointing to head
    dummy = ListNode(0)
    dummy.next = head

    # Step 2: Initialize two pointers
    first = dummy
    second = dummy

    # Step 3: Move 'first' n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Step 4: Move both until 'first' reaches the end
    while first:
        first = first.next
        second = second.next

    # Step 5: Skip the nth node from the end
    second.next = second.next.next

    # Step 6: Return new head
    return dummy.next
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
# n = 2
# result = removeNthFromEnd(node1, n)
# # Printing the result
# current = result
# while current:
#     print(current.val, end=" -> ")
#     current = current.next
# print("None")
# time complexity: O(L), where L is the length of the linked list.
# space complexity: O(1), since we are using only a constant amount of extra space.
# Note: The above code assumes that the input linked list is non-empty and n is valid.