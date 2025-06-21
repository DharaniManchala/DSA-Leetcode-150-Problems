class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    current = head

    while current:
        # Check if it's the start of duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            duplicate_val = current.val
            while current and current.val == duplicate_val:
                current = current.next
            prev.next = current  # Remove all duplicates
        else:
            prev = prev.next
            current = current.next

    return dummy.next
# Example usage:
# Creating a linked list for testing
# node1 = ListNode(1)
# node2 = ListNode(1)
# node3 = ListNode(2)
# node4 = ListNode(3)
# node5 = ListNode(3)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# result = deleteDuplicates(node1)
# # Printing the result
# current = result
# while current:
#     print(current.val, end=" -> ")
#     current = current.next
# print("None")
# time complexity: O(n), where n is the number of nodes in the linked list.
# space complexity: O(1), since we are using only a constant amount of extra space.