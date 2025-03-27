class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)

        # Empty DLL. Could also check if self.head is None
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # One or more nodes
        self.tail.next = new_node
        new_node.next = None
        new_node.previous = self.tail
        self.length += 1
        return


dll = DoublyLinkedList(4)
dll.append_node(5)
dll.print_list()
