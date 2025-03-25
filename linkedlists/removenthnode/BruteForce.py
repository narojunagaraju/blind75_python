# TC: O(n)
# SC: O(1)

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_nth_node_from_end(head: ListNode, n: int) -> ListNode:
    # Counting the number of nodes in the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate the position of the node to remove
    position_to_remove = length - n
    if position_to_remove == 0:
        return head.next

    current = head
    for _ in range(position_to_remove - 1):
        current = current.next

    if current and current.next:
        current.next = current.next.next

    return head


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
