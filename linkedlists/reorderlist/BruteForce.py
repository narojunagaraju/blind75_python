# TC: O(n)
# SC: O(n)
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def re_order_list(head):
    nodes = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i < j:
            nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None


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
