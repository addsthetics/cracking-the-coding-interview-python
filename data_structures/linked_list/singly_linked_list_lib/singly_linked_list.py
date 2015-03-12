from singly_linked_list_lib.singly_linked_list_node import SinglyLinkedListNode


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def add_to_front(self, value):
        """
        O(1)
        """
        temp_node = self.head
        self.head = SinglyLinkedListNode(value)
        self.head.set_next_node(temp_node)
        self.length += 1
        if self.length == 1:
            self.tail = self.head

    def add_to_back(self, value):
        """
        O(1)
        """
        node = SinglyLinkedListNode(value)
        if self.is_empty():
            self.head = node
        else:
            self.tail.set_next_node(node)
        self.tail = node
        self.length += 1

    def add(self, value):
        """
        O(1)
        """
        self.add_to_back(value)

    def remove_front(self):
        if not self.is_empty():
            self.head = self.head.get_next_node()
            self.length -= 1
            if self.length == 0:
                self.tail = None

    def remove_back(self):
        """
        O(n)
        """
        if not self.is_empty():
            if self.length == 1:
                self.tail = None
                self.head = None
            else:
                current = self.head
                while current.get_next_node() is not self.tail:
                    current = current.get_next_node()
                current.next_node = None
                self.tail = current
            self.length -= 1

    def remove(self, item):
        """
        O(n)
        :param item:
        :return:
        """
        if not self.is_empty():
            previous = None
            current_node = self.head
            while current_node is not None:
                if current_node.get_value() == item:
                    if previous is not None:
                        previous.set_next_node(current_node.get_next_node())
                        if current_node.get_next_node() is None:
                            self.tail = previous
                    else:
                        self.remove_front()
                    self.length -= 1
                    return True
                previous = current_node
                current_node = current_node.get_next_node()
        return False

    def clear(self):
        """
        O(1)
        :return:
        """
        self.head = None
        self.tail = None
        self.length = 0

    def enumerate(self):
        """
        O(n)
        :return:
        """
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.get_next_node()

    def __str__(self):
        """
         O(n)
        """
        if not self.is_empty():
            buffer_array = []
            for node in self.enumerate():
                buffer_array.append(str(node))
                buffer_array.append(str('=>'))
            buffer_array.append('None')
            return ''.join(buffer_array)
        else:
            return 'This Linked List is empty!'

