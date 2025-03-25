# TC O(n)
# SC O(1)

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
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


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
