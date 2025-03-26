# TC: O(n)
# SC: O(1)
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def re_order_list(head):
    if not head or not head.next:
        return

    # Find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list in-place
    second_half = reverse_in_place(slow.next)
    slow.next = None

    # Merge the two halves
    merge_linked_lists(head, second_half)


def reverse_in_place(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_linked_lists(first, second):
    l1, l2 = first, second
    while l2:
        l1_next, l2_next = l1.next, l2.next
        l1.next = l2
        l2.next = l1_next
        l1, l2 = l1_next, l2_next


def print_list(head):
    temp = head
    while temp:
        print(temp.value, end=" -> " if temp.next else "")
        temp = temp.next
    print()


if __name__ == "__main__":
    head = ListNode(1)
    first = ListNode(2)
    second = ListNode(3)
    third = ListNode(4)

    head.next = first
    first.next = second
    second.next = third

    re_order_list(head)
    print_list(head)