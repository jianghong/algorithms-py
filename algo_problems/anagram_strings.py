'''
O(nlogn) because sorting
'''

def anagrams(string1, string2):
    return ''.join(sorted(string1)) == ''.join(sorted(string2))


if __name__ == '__main__':
    assert anagrams('pig', 'gip') == True
    assert anagrams('pig', 'gips') == False

