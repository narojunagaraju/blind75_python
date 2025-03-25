# TC  0(n log k)
# SC o(1)

from typing import Optional, List


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    size = len(lists)
    interval = 1

    while interval < size:
        for i in range(0, size - interval, interval * 2):
            lists[i] = merge(lists[i], lists[i + interval])
        interval *= 2

    return lists[0] if size > 0 else None


def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    res = merge_k_lists(lists)

    while res:
        print(res.value, end=" -> " if res.next else "\n")
        res = res.next
