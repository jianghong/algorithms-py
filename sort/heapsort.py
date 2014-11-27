import sys
sys.path.insert(0, '../data_structures')

from heap import Heap

def sort(array):
    heapified = Heap(array)
    result = []

    while heapified.get_size() > 0:
        result.append(heapified.extract())

    return result

if __name__ == '__main__':
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([4, 5, 4, 1, 9, 4, 10, 4]) == [1, 4, 4, 4, 4, 5, 9, 10]
    assert sort([2, 3, 4, 1]) == [1, 2, 3, 4]