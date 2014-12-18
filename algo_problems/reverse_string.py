def reverse_string(string):
    res = ''

    for i in xrange(len(string)-1, -1, -1):
        res += string[i]

    return res

if __name__ == '__main__':
    assert reverse_string('abcd') == 'dcba'
