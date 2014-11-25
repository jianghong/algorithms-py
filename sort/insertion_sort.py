def sort(array):

    for k in xrange(1, len(array)):
        i = k
        while i > 0 and array[i-1] > array[i]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1

    print array
    return array



if __name__ == '__main__':
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 2, 1]) == [1, 2, 3]
