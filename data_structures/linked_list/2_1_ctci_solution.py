from singly_linked_list_lib.singly_linked_list import SinglyLinkedList


def remove_duplicates(head_node):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)?
    """
    #TODO: Compare my solution
    if head_node is None:
        return 'This is empty!'

    current_node = head_node

    while current_node is not None:
        runner = current_node
        while runner.get_next_node() is not None:
            if runner.get_next_node().get_value() == current_node.get_value():
                runner.set_next_node(runner.get_next_node().get_next_node())
            else:
                runner = runner.get_next_node()
        current_node = current_node.get_next_node()


def main():
    list1 = SinglyLinkedList()
    list1.add("P")
    list1.add("O")
    list1.add("P")
    list1.add(" ")
    list1.add("F")
    list1.add("O")
    list1.add("L")
    list1.add("L")
    list1.add("O")
    list1.add("W")
    list1.add(" ")
    list1.add("M")
    list1.add("E")
    print(list1)
    remove_duplicates(list1.head)
    print(list1)


if __name__ == "__main__":
    main()