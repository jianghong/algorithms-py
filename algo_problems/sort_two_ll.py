from data_structures.linked_list import *
import pdb

'''
Sort and merge two sorted Linked Lists into one.
Implementation keeps two linked lists intact.
n = size of ll1
m = size of ll2
O(n + m)
'''


def sort_and_merge_ll(ll1, ll2):
    ll3 = SinglyLinkedList()
    walker1 = ll1.sentinel.next
    walker2 = ll2.sentinel.next
    walker3 = ll3.sentinel
    walker1_done = False
    walker2_done = False

    while not walker1_done and not walker2_done:
        if walker1.value <= walker2.value:
            next = walker1
            walker3.next = walker1
            walker1 = walker1.next
            next.next = ll3.sentinel

        elif walker2.value < walker1.value:
            next = walker2
            walker3.next = walker2
            walker2 = walker2.next
            next.next = ll3.sentinel

        walker3 = walker3.next
        if walker1 == ll1.sentinel:
            walker1_done = True
        if walker2 == ll2.sentinel:
            walker2_done = True

    if walker1_done:
        while walker2 != ll2.sentinel:
            next = walker2
            walker3.next = next
            walker2 = walker2.next
            next.next = ll3.sentinel
    else:
        while walker1 != ll1.sentinel:
            next = walker1
            walker3.next = walker1
            walker1 = walker1.next
            next.next = ll3.sentinel
    return ll3

if __name__ == '__main__':
    ll1 = SinglyLinkedList()
    ll1.mass_insert([1, 3, 5, 7])
    ll2 = SinglyLinkedList()
    ll2.mass_insert([2, 4, 6, 8])
    assert sort_and_merge_ll(ll1, ll2).to_array() == [1, 2, 3, 4, 5, 6, 7, 8]


    ll1 = SinglyLinkedList()
    ll1.mass_insert([6, 7, 9, 10])
    ll2 = SinglyLinkedList()
    ll2.mass_insert([1, 2, 3, 11])
    assert sort_and_merge_ll(ll1, ll2).to_array() == [1, 2, 3, 6, 7, 9, 10, 11]