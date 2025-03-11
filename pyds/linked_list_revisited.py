class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # Create new node
        new_node = Node(value)

        # Empty case
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            return

        # Not empty case
        self.tail.next = new_node
        self.tail = new_node

        # Update length
        self.length += 1

    def pop(self):
        # Empty case
        if self.length == 0:
            return

        # One node case
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        # More items case
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1


test = LinkedList(5)
test.pop()
test.print_list()
