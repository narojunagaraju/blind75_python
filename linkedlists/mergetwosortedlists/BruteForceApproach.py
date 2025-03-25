# TC: O((m + n) log (m + n))
# SC : O(m+n)

from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_list = []

    current = list1
    while current:
        merged_list.append(current.value)
        current = current.next

    current = list2
    while current:
        merged_list.append(current.value)
        current = current.next

    merged_list.sort()
    dummy = ListNode()
    current = dummy

    for value in merged_list:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


if __name__ == "__main__":
    head1 = ListNode(1)
    second = ListNode(2)
    third = ListNode(4)
    head1.next = second
    second.next = third

    head2 = ListNode(1)
    second2 = ListNode(3)
    third2 = ListNode(4)
    head2.next = second2
    second2.next = third2

    res = merge_two_lists(head1, head2)
    while res:
        print(res.value)
        res = res.next
