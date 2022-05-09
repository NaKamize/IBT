# Author: Jozef Makiš
# License: GPLv3
# File: DLL.py

class Node:
    """ Node class with his pointers to next and previous node. Node saves data, that are tokens."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    """ Doubly linked list with his head node. It is deep pushdown for syntax analysis.
    Some operations are from https://www.geeksforgeeks.org/doubly-linked-list/.
    Cited 20.3. 2022, Author: GeeksforGeeks """
    def __init__(self):
        self.head = None

    """ Method pushes node into list. """
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    """ Method pops node from the top. """
    def pop(self):
        popped = self.head
        if self.head is None:
            print("List is empty")
            return
        new_head = self.head.next
        if self.dll_len(self.head) != 1:
            new_head.prev = None
        self.head = new_head
        return popped

    """ Method inserts node into list, before specified previous node. """
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
        return new_node

    """ Remove specified node from the list. """
    def remove(self, node):
        temp_head = self.head
        while temp_head:
            if temp_head == node:
                break
            temp_head = temp_head.next
        node_prev = node.prev
        if node_prev is not None:
            node_prev.next = node.next

    """ Append node into list. """
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

    """ Print content of the list. """
    def printList(self, node):
        if node is None:
            print("Node is empty.")
            return
        while node:
            print(node.data)
            node = node.next

    """ Returns true if list is empty. """
    def not_empty(self):
        return self.head is not None

    """ Returns length of the list. """
    def dll_len(self, node):
        length = 0
        while node:
            node = node.next
            length += 1
        return length
