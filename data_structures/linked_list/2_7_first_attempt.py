from singly_linked_list_lib.singly_linked_list import SinglyLinkedList


def is_palindrome(head_node):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    NOTE: Close to CTCI solution
    """
    if head_node is None:
        return None
    if head_node.get_next_node() is None:
        return True
    buffer = []
    current_node = head_node
    while current_node is not None:
        buffer.append(current_node.get_value())
        current_node = current_node.get_next_node()
    #Could Move the reverse '[::-1] to it's on O(n) function
    return "".join([str(x) for x in buffer]) == "".join([str(y) for y in buffer[::-1]])


def main():
    list1 = SinglyLinkedList()
    list1.add('a')
    list1.add('b')
    list1.add('d')
    list1.add('e')
    print(list1)
    #False
    print(is_palindrome(list1.head))
    list2 = SinglyLinkedList()
    list2.add(2)
    list2.add(1)
    list2.add(2)
    #True
    print(is_palindrome(list2.head))
    list2.add('3')
    #False
    print(is_palindrome(list2.head))
    list3 = SinglyLinkedList()
    list3.add('a')
    list3.add('b')
    list3.add('d')
    list3.add('b')
    list3.add('a')
    #True
    print(is_palindrome(list3.head))

if __name__ == '__main__':
    main()