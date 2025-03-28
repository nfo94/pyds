import logging


logging.basicConfig(encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)


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

    def log_list(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.value)
            current = current.next

        logger.info(f" {items}")

    def get_length(self):
        return self.length

    def append_node(self, value):
        # Create new node
        new_node = Node(value)

        # Empty case
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # Not empty case
        self.tail.next = new_node
        self.tail = new_node

        # Update length
        self.length += 1

    def pop_last_node(self):
        # Empty case
        if self.length == 0:
            return

        # One node case
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        # More than one node case
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        self.tail = previous_node
        self.tail.next = None
        self.length -= 1

    def prepend_node(self, value):
        new_node = Node(value)

        # Empty case
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # More nodes case
        old_head_node = self.head
        self.head = new_node
        new_node.next = old_head_node
        self.length += 1

    def pop_first_node(self):
        # Empty case
        if self.length == 0:
            return

        # One node case
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        # More nodes case
        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        self.length -= 1

    # This is not an index like in arrays, here we simulate an index by traversing
    # the linked list using a variable
    def get_node_by_index(self, index):
        if not isinstance(index, int) or index < 0 or index >= self.length:
            length = self.get_length()
            logger.info(f" Provide a positive integer starting from 0 to {length - 1}.")
            return

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def set_value_by_index(self, index, value):
        node = self.get_node_by_index(index)

        if node:
            node.value = value
            return

    def insert_node_by_index(self, index, value):
        if not isinstance(index, int) or index < 0 or index > self.length:
            logger.info(" Provide a positive integer starting from 0.")
            return

        # Prepend case, will always be a prepend if the index is 0
        if index == 0:
            self.prepend_node(value)
            return

        # Append case
        if index == self.length:
            self.append_node(value)
            return

        new_node = Node(value)
        # Empty case
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # More nodes case
        current_node = self.head
        previous_node = self.head
        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = new_node
        new_node.next = current_node
        self.length += 1

    def remove_node_by_index(self, index):
        if not isinstance(index, int) or index < 0 or index >= self.length:
            logger.info(" Provide a positive integer starting from 0.")
            return

        # Empty case. Doesn't matter the index
        if self.length == 0:
            return

        # If index is zero it means we want to pop the first node
        if index == 0:
            self.pop_first_node()
            return

        if index == self.length - 1:
            self.pop_last_node()
            return

        # More nodes case
        # current_node = self.head
        # previous_node = self.head
        # for _ in range(index):
        #     previous_node = current_node
        #     current_node = current_node.next

        # previous_node.next = current_node.next
        # current_node.next = None

        # Using get_node_by_index
        previous_node = self.get_node_by_index(index - 1)
        node_to_remove = previous_node.next
        previous_node.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return

        # We can change these items without messing up with anything else
        current_node = self.head
        self.head = self.tail
        self.tail = current_node

        # This is tricky to reason!
        after_node = current_node.next
        previous_node = None
        for _ in range(self.length):
            # First, move the after node since any change would mess up the location
            after_node = current_node.next
            # Reversing
            current_node.next = previous_node
            # Moving the loop
            previous_node = current_node
            current_node = after_node


test = LinkedList(5)
test.append_node(4)
test.append_node(3)
test.append_node(2)
test.log_list()
test.reverse()
test.log_list()
