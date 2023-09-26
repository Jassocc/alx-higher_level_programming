#!/usr/bin/python3
"""
Module 7
definition of node
definition of singlylinkedlist
"""


class Node:
    """
    define Node
    """
    def __init__(self, data, next_node=None):
        """
        initialiser of Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        retrieves the data
        """
        ar = self.__data
        return ar

    @data.setter
    def data(self, value):
        """
        sets the data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        retrieves next_node
        """
        ab = self.__next_node
        return ab

    @next_node.setter
    def next_node(self, value):
        """
        sets the next_node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    definition of singly linked list
    """
    def __init__(self):
        """
        initialiser of singly linked list
        """
        self.__head = None

    def __str__(self):
        """
        representation of singly linked list
        """
        res = ""
        curr = self.__head
        while curr is not None:
            res += str(curr.data) + "\n"
            curr = curr.next_node
        return res.strip()

    def sorted_insert(self, value):
        """
        inserts data into list in sorted formation
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        curr = self.__head
        while curr.next_node is not None and curr.next_node.data < value:
            curr = curr.next_node
        new_node.next_node = curr.next_node
        curr.next_node = new_node
