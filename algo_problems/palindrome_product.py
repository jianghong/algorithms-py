'''
A palindromic number reads the same both ways. 

Find the largest palindrome made from the product of two n-digit numbers.
'''


def is_palindrome(n):
    n = str(n)
    mid_i = len(n) // 2
    for i in xrange(int(mid_i)):
        if n[i] != n[-1 - i]:
            return False
    return True


def largest_palindrome(n):
    n1 = int('9' * n)
    n2 = int('9' * n)
    min_n = int('1' + ('0' * (n - 1)))

    for i in xrange(n1, min_n, -1):
        for j in xrange(n2, min_n, -1):
            res = i * j
            if is_palindrome(res):
                print 'i : ' + str(i) + ' j + ' + str(j)
                return res

if __name__ == '__main__':
    assert is_palindrome(2002) == True
    assert is_palindrome(1234) == False
    assert largest_palindrome(2) == 9009
    print largest_palindrome(3)
    print largest_palindrome(4)
    print largest_palindrome(10)
