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
        # None is the "last next" (end of the linked list)
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        To append a new node we need to create a new node with the received
        value and check if it's the first node. If yes, assign it to the head
        and tail. If not, assign it to next using tail, which is the last node.
        Finally, increment the length of the linked list
        """
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
        # First we need to check if the linked list is empty
        if self.length == 0:
            return None
        # If not, we'll start from the beginning of the list (head) and iterate
        temp = self.head
        # This variable will be used to keep track of the previous node
        pre = self.head
        # While there's still a value (not None) we'll keep iterating
        while temp.next:
            pre = temp
            temp = temp.next
        # The tail is the previous node since temp.next reached None
        self.tail = pre
        # Last node points to None
        self.tail.next = None
        # New length since we'll remove the last node (length - 1)
        self.length -= 1
        # If subtracting the length makes it 0, we need to set head and tail to
        # None, since there's no nodes left
        if self.length == 0:
            self.head = None
            self.tail = None
        # Return the removed node. temp was removed since tail.next now points
        # to None
        return temp.value

    def prepend(self, value):
        # We'll add a new node to the beginning of the linked list
        new_node = Node(value)
        # Before doing anything with the new node, first check if the linked
        # list is empty
        if self.length == 0:
            # If it's empty then assign the new node to head and tail
            self.head = new_node
            self.tail = new_node
        # If it's not empty, we'll assign the current head of the linked list
        # to new_node.next, to make the new node point to the correct next node
        else:
            new_node.next = self.head
            # Now assign the new node as the new head of the linked list
            self.head = new_node
        # Finally, increment the length of the linked list
        self.length += 1
        return True

    def pop_first(self):
        # First, check if the linked list is empty
        if self.length == 0:
            # If it is, return None, since we can't pop anything
            return None
        # Assign the head to a temporary variable
        temp = self.head
        # Assign head.next as the new head, since we want to pop the first node
        self.head = self.head.next
        # Now assign None to temp.next, since it won't point to anything
        temp.next = None
        # Decrement the length of the linked list, since we popped the first
        # node
        self.length -= 1
        # If after the decrement the length is 0, meaning, the linked list now
        # is empty and before it had only one node and we popped it, we need to
        # set the tail to None. We don't need to set the head to None since we
        # already did that in line 111 (in the case that the linked list had
        # one node)
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


my_linked_list = LinkedList("value")
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.pop()
# my_linked_list.prepend(3)
my_linked_list.print_list()
print(my_linked_list.length)
my_linked_list.pop_first()
my_linked_list.print_list()
print(my_linked_list.length)
