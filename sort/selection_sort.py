def sort(array):
    for i in xrange(len(array)):
        min_index = i
        for j in xrange(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    print array
    return array

if __name__ == '__main__':
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([4, 5, 4, 1, 9, 4, 10, 4]) == [1, 4, 4, 4, 4, 5, 9, 10]