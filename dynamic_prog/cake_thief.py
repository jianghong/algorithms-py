'''
Problem: https://www.interviewcake.com/question/cake-thief
'''


def max_duffel_bag_value(cake_types, max_capacity):
    store = [0] * (max_capacity+1)
    cake_store = {cake_type[0]: cake_type[1] for cake_type in cake_types}

    for i in xrange(1, max_capacity+1):
        v = -1
        cake_value = cake_store.get(i, 0)
        for j in xrange(i):
            v = max(store[j] + store[i-j], cake_value, v)

        store[i] = v

    return store[max_capacity]

if __name__ == '__main__':
    ct = [(7, 160), (3, 90), (2, 15)]

    assert max_duffel_bag_value(ct, 4) == 90
    assert max_duffel_bag_value(ct, 20) == 555
    assert max_duffel_bag_value(ct, 5) == 105
    assert max_duffel_bag_value(ct, 7) == 180
    assert max_duffel_bag_value(ct, 0) == 0
