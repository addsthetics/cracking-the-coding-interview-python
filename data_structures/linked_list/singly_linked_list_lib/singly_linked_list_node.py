class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node

    def __str__(self):
        return self.value