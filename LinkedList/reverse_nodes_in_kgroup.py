class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Helper to get kth node from a starting point
    def get_kth_node(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        kth = get_kth_node(group_prev, k)
        if not kth:
            break

        group_next = kth.next

        # Reverse the group
        prev = group_next
        curr = group_prev.next

        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Reconnect with previous part
        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

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
# k = 2
# result = reverseKGroup(node1, k)
# # Printing the result
# current = result
# while current:
#     print(current.val, end=" -> ")
#     current = current.next
# print("None")
# of nodes.
# time complexity: O(n), where n is the number of nodes in the linked list.
# space complexity: O(1), since we are reversing the nodes in place without using extra space.