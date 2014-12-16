class SentinelNode:

    def __init__(self):
        self.next = self
        self.prev = self


class LinkedNode:

    def __init__(self, value=None):
        self.next = None
        self.value = value


class SinglyLinkedList:

    def __init__(self):
        self.sentinel = SentinelNode()

    def mass_insert(self, value_list):
        for value in value_list:
            self.insert(LinkedNode(value))

    def insert(self, new_node):
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node

    def search(self, value):
        walker = self.sentinel.next
        while walker != self.sentinel:
            if value == walker.value:
                return walker

            walker = walker.next

        return None

    def delete(self, node):
        self.sentinel.next =  node.next

    def pop(self):
        popping = self.sentinel.next
        self.sentinel.next = popping.next
        return popping

    def to_array(self):
        result = []
        walker = self.sentinel.next
        while walker != self.sentinel:
            result.append(walker.value)
            walker = walker.next

        return result

if __name__ == '__main__':
    sl = SinglyLinkedList()
    sl.insert(LinkedNode(1))
    sl.mass_insert([3, 4, 5, 5, 6, 4, 1])
    assert sl.to_array() == [1, 4, 6, 5, 5, 4, 3, 1]
    assert sl.sentinel.next.value == 1
    assert sl.pop().value == 1
    assert sl.to_array() == [4, 6, 5, 5, 4, 3, 1]
    assert sl.search('nope') == None
    assert sl.search(5).value == 5
    sl.delete(sl.search(4))
    assert sl.to_array() == [6, 5, 5, 4, 3, 1]


