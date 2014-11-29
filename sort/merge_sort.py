import math

def sort(array):
    size = len(array)

    if size == 1:
        return array

    else:
        middle = int(math.ceil(size/2))
        subarray1 = sort(array[:middle])
        subarray2 = sort(array[middle:])
        return merge(subarray1, subarray2)


def merge(subarray1, subarray2):
    merged = []

    while len(subarray1) and len(subarray2):
        if subarray1[0] <= subarray2[0]:
            merged.append(subarray1.pop(0))
        else:
            merged.append(subarray2.pop(0))

    if len(subarray1):
        merged += subarray1
    else:
        merged += subarray2

    return merged

if __name__ == '__main__':
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([4, 5, 4, 1, 9, 4, 10, 4]) == [1, 4, 4, 4, 4, 5, 9, 10]
    assert sort([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert sort([9, 8, 1, 5]) == [1, 5, 8, 9]