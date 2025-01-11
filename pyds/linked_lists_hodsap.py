class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


words = SinglyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")

for word in words.iter():
    print(word)
