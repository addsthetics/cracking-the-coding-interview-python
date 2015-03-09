from singly_linked_list_lib.singly_linked_list import SinglyLinkedList


def remove_duplicates(head_node):
    """
    Time Complexity:
    Space Complexity:
    """
    if head_node == None:
        return 'This is empty!'

    char_dict = dict()

    char_dict[head_node.get_value()] = True
    previous_node = head_node
    current_node = head_node.get_next_node()

    while current_node is not None:
        if current_node.get_value() in char_dict:
            previous_node.set_next_node(current_node.get_next_node())
        else:
            char_dict[current_node.get_value()] = True
            previous_node = current_node
        current_node = current_node.get_next_node()


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
    print(list1)
    remove_duplicates(list1.head)
    print(list1)

if __name__ == "__main__":
    main()