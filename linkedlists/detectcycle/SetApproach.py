# TC O(n)
# SC O(n)

from typing import Optional, Set

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    visited: Set[ListNode] = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False


if __name__ == "__main__":
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second  # Creates a cycle

    print(has_cycle(head))