from data_structures.linked_list import *

'''
O(n): while look and recusion will run at most n times in total because
_helper will skip nodes until the next available non duplicate and the 
while loop continues from there. There is no repeat or overlap between _helper
and the while loop.
'''
def remove_duplicates_from_ll(ll):
    # first value in ll can't be duplicate
    store = {ll.sentinel.next.value: 1}

    def _helper(node, store):
        if node.next == ll.sentinel:
            return ll.sentinel
        elif store.get(node.next.value):
            return _helper(node.next, store)
        store[node.next.value] = 1
        return node.next

    walker = ll.sentinel.next
    while walker != ll.sentinel:
        walker.next = _helper(walker, store)
        walker = walker.next

    return sl

if __name__ == '__main__':
    sl = SinglyLinkedList()
    sl.mass_insert([1, 4, 5, 1])
    print remove_duplicates_from_ll(sl).to_array()
    assert remove_duplicates_from_ll(sl).to_array() == [1 ,4, 5]

    sl = SinglyLinkedList()
    sl.mass_insert([1, 4, 5, 4, 1, 2, 2])
    print remove_duplicates_from_ll(sl).to_array()
    assert remove_duplicates_from_ll(sl).to_array() == [1 ,4, 5, 2]
