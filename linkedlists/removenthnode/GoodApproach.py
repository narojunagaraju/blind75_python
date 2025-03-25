# TC: O(n)
# SC: O(1)

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_nth_node_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n steps ahead
    for _ in range(n):
        if first:
            first = first.next

    # Move both pointers until the first pointer reaches the end
    while first and first.next:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    if second and second.next:
        second.next = second.next.next

    return dummy.next


def print_list(head: ListNode):
    current = head
    while current:
        print(current.value)
        current = current.next


# Creating the linked list
head = ListNode(1)
first = ListNode(2)
second = ListNode(3)
third = ListNode(4)
fourth = ListNode(5)

head.next = first
first.next = second
second.next = third
third.next = fourth

# Remove the nth node from the end
n = 2
new_head = remove_nth_node_from_end(head, n)

# Print the modified linked list
print_list(new_head)