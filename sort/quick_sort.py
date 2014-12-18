
def sort(array):
    if not array:
        return []

    else:
        pivot = array[0] # choice of pivot can be improved here
        less = [x for x in array[1:] if x < pivot]
        more = [x for x in array[1:] if x >= pivot]
        return sort(less) + [pivot] + sort(more)

if __name__ == '__main__':
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([4, 5, 4, 1, 9, 4, 10, 4]) == [1, 4, 4, 4, 4, 5, 9, 10]