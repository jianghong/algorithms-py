def sort(array):

    l = len(array)

    while l > 1:
        for i in xrange(l-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        l -= 1

    print array
    return array


if __name__ == '__main__':
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([4, 5, 4, 1, 9, 4, 10, 4]) == [1, 4, 4, 4, 4, 5, 9, 10]
    assert sort([2, 3, 4, 1]) == [1, 2, 3, 4]