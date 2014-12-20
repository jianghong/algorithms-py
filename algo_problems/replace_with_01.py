'''
Replace wild cards with all possible combinations of zeros and ones using recursion.
'''


def replace(in_str):
    result = ''

    wild_card_i = in_str.find('*')

    if wild_card_i < 0:
        result += ' ' + in_str
        return result

    result  += replace(in_str[:wild_card_i] + '0' + in_str[wild_card_i+1:])
    result  += replace(in_str[:wild_card_i] + '1' + in_str[wild_card_i+1:])

    return result


if __name__ == '__main__':
    assert replace('0*1*') == ' 0010 0011 0110 0111'
    assert replace('0000') == ' 0000'
    assert replace('**') == ' 00 01 10 11'
    print replace('1***1')
    assert replace('1***1') == ' 10001 10011 10101 10111 11001 11011 11101 11111'
