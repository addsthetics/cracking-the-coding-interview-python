from singly_linked_list_lib.singly_linked_list import SinglyLinkedList


def find_kth_last(head_node, k):
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if k <= 0:
        return None

    p1 = head_node
    p2 = head_node

    for i in range(k - 1):
        if p2 is None:
            return None
        p2 = p2.get_next_node()
    if p2 is None:
        return None

    while p2.get_next_node() is not None:
        p1 = p1.get_next_node()
        p2 = p2.get_next_node()
    return p1

def main():
    list1 = SinglyLinkedList()
    list1.add("F")
    list1.add("O")
    list1.add("L")
    list1.add("L")
    list1.add("O")
    list1.add("W")
    list1.add(" ")
    list1.add("U")
    list1.add("P")
    print(find_kth_last(list1.head, 2).value == "U")
    print(find_kth_last(list1.head, 9).value == "F")
    print(find_kth_last(list1.head, 10) is None)
if __name__ == "__main__":
    main()