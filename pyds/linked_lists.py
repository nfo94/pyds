# Does not have indexes
# Nodes are spread all over the memory
# The head points to the first node
# The tail points to the last node
# Each node points to the next node
# Last node points to None


# Since we'll need to create nodes to fill the linked list we might as well
# create an object for it
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """
        Initiate the linked list with received value. The new value will be
        the head and tail of the linked list since it's the first value
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        To print the list we need to start the iteration from the head, so we
        assign the head to a temporary variable and then iterate through the
        nodes, allways assigning the next node to the temporary variable
        """
        temp = self.head
        # None is the tail of the linked list
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """ """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp.value


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)

my_linked_list.print_list()
print(my_linked_list.print_list())
