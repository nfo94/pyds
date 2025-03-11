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

        logger.info(f"\n{items}")

    def get_length(self):
        logger.info(f"\n{self.length}")

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

        # More than one node case
        current_node = self.head
        node_before = self.head
        while current_node.next:
            node_before = current_node
            current_node = current_node.next

        self.tail = node_before
        self.tail.next = None
        self.length -= 1

    def prepend(self, value):
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

    def pop_first(self):
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
    # the linked list using a variable that corresponds to the number of iteractions
    # that we will need to do
    def get_by_index(self, index):
        if not isinstance(index, int) or index < 0 or index >= self.length:
            logger.info("\nProvide a positive integer starting from 0.")
            return

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        logger.info(f"\n{current_node.value}")


test = LinkedList(5)
test.append(4)
test.append(3)
test.append(2)
test.append(1)
test.get_by_index(1)
