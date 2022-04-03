class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, prev_node, data):
        if prev_node is None:
            print("Prev node neexistuje.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, data):
        new_node = Node(data)
        new_node.next = None
        node = self.head

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while node.next is not None:
            node = node.next

        node.next = new_node
        new_node.prev = node

    def printList(self, node):
        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node.next
