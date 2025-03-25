# TC  0(n log k)
# SC o(k)

from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __lt__(self, other):
        return self.value < other.value


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)

    dummy = ListNode(0)
    current = dummy

    while heap:
        smallest = heapq.heappop(heap)
        current.next = smallest
        current = current.next
        if smallest.next:
            heapq.heappush(heap, smallest.next)

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
