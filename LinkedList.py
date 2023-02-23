#Name: sophiacphilips
#GitHub Username: sophiacphilips
#Date: 02/22/23
#This code is designed to utilize an ADT linked list and manipulate the list values provided by the user via recursion.


class Node:
    """represents node in a linked list"""
    def __init__(self, data):
        self.data= data
        self.next = None

class LinkedList:
    """
    a linked list implementation of the list ADT
    """
    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def rec_add(self, a_node, val):
        """
        adds a node to the end of a val containing a linked list
        """
        if a_node is None:
            return Node(val)
        else:
            a_node.next = self.rec_add(a_node.next, val)
            return a_node

    def add(self, val):
        """
        recursive add helper method

        """
        self._head = self.rec_add(self._head, val)

    def insert(self, val, pos):
        """ helper recursive insert method"""
        self._head = self.add_insert(self._head, val, pos)

    def add_insert(self, a_node, val, pos):
        """recursive insert method"""
        if a_node is None:
            return Node(val)
        if pos == 0:
            n = Node(val)
            n.next = a_node
            return n
        else:
            a_node.next = self.add_insert(a_node.next, val, pos-1)
            return a_node

    def rec_remove(self, a_node, val):
        """recursive remove method"""
        if a_node is None:
            return a_node
        elif a_node.val == val:
            return a_node.next
        else:
            a_node.next = self.rec_remove(a_node.next, val)
            return a_node

    def remove(self, val):
        """helper recursive remove method"""
        self._head = self.rec_remove(self._head, val)

    def rec_contains(self, a_node, val):
        """recursive contains method"""
        if a_node is None:
            return False
        if a_node.data == val:
            return True
        return self.rec_contains(a_node.next, val)

    def contains(self, val):
        """helper recursive contains method"""
        return self.rec_contains(self._head, val)

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)

    def rec_reverse(self, node):
        """recursive reverse method"""
        if node is None or node.next is None:
            return node
        next_node= node.next
        rem = self.rec_reverse(node.next)
        next_node.next = node
        node.next = None
        return rem

    def reverse(self):
        """recursive reverse helper method"""
        self._head = self.rec_reverse(self._head)

    def rec_to_plain_list(self, node, result):
        """recursive list method to return plain list"""
        if node is None:
            return result
        result.append(node.data)
        return self.rec_to_plain_list(node.next, result)

    def to_plain_list(self):
        """recursive helper list"""
        result=[]
        self.rec_to_plain_list(self._head, result)
        return result

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None