from data_structures.linked_list import *

WHITE = 0
GRAY = 1
BLACK = 2


class Node:

    def __init__(self, value=None):
        self.value = value
        self.color = WHITE
        self.distance = -1
        self.parent = None


class Graph:

    def __init__(self):
        self.adj_list = []


if __name__ == '__main__':
    g = Graph()
    g.adj_list = [
        SinglyLinkedList().mass_insert('r', 'w', 's'),
        SinglyLinkedList().mass_insert('v', 's', 'r'),
        SinglyLinkedList().mass_insert('r', 'v'),
        SinglyLinkedList().mass_insert('s', 't', 'w'),
        SinglyLinkedList().mass_insert('w', 't', 'x'),
        SinglyLinkedList().mass_insert('w' 'x', 't'),
        SinglyLinkedList().mass_insert('t', 'y', 'u'),
        SinglyLinkedList().mass_insert('x', 'u', 'y'),
    ]
