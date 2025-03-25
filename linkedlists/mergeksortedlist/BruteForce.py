# TC 0(n log n)
# SC o(n)

from typing import Optional, List


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    values = []

    for node in lists:
        while node:
            values.append(node.value)
            node = node.next

    values.sort()

    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next

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
