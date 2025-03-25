# TC O(n)
# SC O(n)
from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(head: Optional[ListNode]) -> None:
    root = head
    while root:
        print(root.value)
        root = root.next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    reversed_head = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return reversed_head


if __name__ == "__main__":
    head = ListNode(1)
    first = ListNode(2)
    second = ListNode(3)
    third = ListNode(4)
    fourth = ListNode(5)

    head.next = first
    first.next = second
    second.next = third
    third.next = fourth

    print_list(head)
    print("---------------")
    reverse_head = reverse_list(head)
    print_list(reverse_head)
