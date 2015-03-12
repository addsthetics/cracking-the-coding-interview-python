from singly_linked_list_lib.singly_linked_list import SinglyLinkedList


def find_kth_last(head_node, k):
    """
    Time Complexity: O(N
    Space Complexity:O(1)
    """
    if head_node == None:
        return None
    #Calculate Length
    length = 0
    current_node = head_node
    while current_node is not None:
        current_node = current_node.get_next_node()
        length += 1
    if length < k:
        return None

    res_node = head_node
    for i in range(length - k):
        res_node = res_node.get_next_node()
    return res_node


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