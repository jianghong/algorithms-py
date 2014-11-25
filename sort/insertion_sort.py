def insertion_sort(array):

    for k in xrange(1, len(array)):
        i = k
        while i > 0 and array[i-1] > array[i]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1

    print array
    return array



if __name__ == '__main__':
    insertion_sort([2, 1])
    insertion_sort([3, 2, 1])
