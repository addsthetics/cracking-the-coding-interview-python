from singly_linked_list_lib.singly_linked_list import SinglyLinkedList
from singly_linked_list_lib.singly_linked_list_node import SinglyLinkedListNode


def delete_node_middle(node):
    if node is None or node.get_next_node() is None:
        return
    node.set_value(node.next_node.value)
    node.set_next_node(node.next_node.next_node)

def main():
    list1 = SinglyLinkedList()
    list1.add('a')
    list1.add('b')
    node_to_delete1 = SinglyLinkedListNode('c')
    list1.add_node(node_to_delete1)
    list1.add('d')
    list1.add('e')
    print(list1)
    delete_node_middle(node_to_delete1)
    print(list1)

if __name__ == '__main__':
    main()