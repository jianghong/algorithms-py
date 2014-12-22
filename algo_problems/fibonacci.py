'Return the n-th fibonacci number.'


def fibonacci(n):
    store = [0] * (n+1)
    def _helper(n, store):
        if n == 0 or n == 1:
            store[n] = n
        else:
            store[n] = store[n-2] + store[n-1]

    for i in xrange(n+1):
        _helper(i, store)

    return store[n]
if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
