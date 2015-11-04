# http://www.checkio.org/mission/good-radix

import string

def checkio(number):
    d = {c: i for i, c in enumerate(string.digits + string.ascii_uppercase)}

    for radix in range(max(map(d.get, number))+1, 37):
        n = sum(d[c]*radix**i for i, c in enumerate(number[::-1]))

        if n % (radix-1) == 0:
            return radix

    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')
