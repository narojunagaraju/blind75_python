# TC: O((m + n)
# SC : O(1)


from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    l1, l2 = list1, list2

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

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
