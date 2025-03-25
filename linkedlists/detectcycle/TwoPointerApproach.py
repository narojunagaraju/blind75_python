# TC O(n)
# SC O(1)

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

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