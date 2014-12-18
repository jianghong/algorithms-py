'''
O(n) on average assuming good hash chaining.
'''


def string_has_duplicate_chars(string):
    store = {}
    for char in string:
        if store.get(char, None):
            return True
        store[char] = 1
    return False


def remove_duplicate_chars(string):
    store = {}
    res = ''
    for char in string:
        if not store.get(char, None):
            store[char] = 1
            res += char
    return res

if __name__ == '__main__':
    assert string_has_duplicate_chars('aaaca') == True
    assert string_has_duplicate_chars('bcbcbc') == True
    assert string_has_duplicate_chars('abcdef') == False

    assert remove_duplicate_chars('aaca') == 'ac'
    assert remove_duplicate_chars('abcda') == 'abcd'
    assert remove_duplicate_chars('abcd') == 'abcd'
    assert remove_duplicate_chars('') == ''
    assert remove_duplicate_chars('a') == 'a'
