import math

"""
More explicitly, this is an implementation of a binary min-heap. Using an array as the data structure.
"""
class Heap:
    def __init__(self, array=None):
        self.heap = [] if array == None else array
        self.size = len(self.heap)
        self.build_heap()

    def log(self):
        print self.heap
        return self.heap

    def get_current(self, i):
        return self.heap[i]

    def get_left_child(self, i):
        if (2*i+1) < self.size:
            return self.heap[2*i+1]

    def get_right_child(self, i):
        if (2*i+2) < self.size:
            return self.heap[2*i+2]

    def build_heap(self):
        for i in xrange(int(math.floor(self.size / 2))-1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        smallest_i = i
        if self.get_left_child(i) and self.get_left_child(i) < self.get_current(smallest_i):
            smallest_i = 2*i + 1
        if self.get_right_child(i) and self.get_right_child(i) < self.get_current(smallest_i):
            smallest_i = 2*i + 2

        if smallest_i != i:
            print "Old: {0}".format(self.heap)
            if smallest_i == 2*i + 1:
                print " >> Swapping Left Child: {0} with {1}".format(self.get_left_child(i),
                                                                     self.get_current(i))
            else:
                print " >> Swapping Right Child: {0} with {1}".format(self.get_right_child(i), 
                                                                     self.get_current(i))
            self.heap[i], self.heap[smallest_i] = self.heap[smallest_i], self.heap[i]
            print "New: {0}".format(self.heap)
            self.min_heapify(smallest_i)

    def verify_min_heap(self):
        for i in xrange(int(math.floor(self.size / 2))):
            if (self.get_left_child(i) and self.get_left_child(i) < self.get_current(i)) or \
               (self.get_right_child(i) and self.get_right_child(i) < self.get_current(i)):
                return False
        return True


if __name__ == '__main__':
    assert Heap([2, 1]).verify_min_heap()
    assert Heap([4, 1, 5]).verify_min_heap()
    assert Heap([5, 4, 3, 2, 1]).verify_min_heap()
    assert Heap([1, 2, 10, 9, 4, 2, 4, 20, 19, 18, 4]).verify_min_heap()