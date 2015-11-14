# http://www.checkio.org/mission/number-factory/

# ref: http://stackoverflow.com/a/16007256
def checkio(number):

    factors = []

    while number > 1:
        for i in range(9, 1, -1):
            if number % i == 0:
                factors.append(i)
                number /= i
                break
        else:
            # prime factor > 9
            factors.append(0)
            break

    if 0 not in factors:
        return int(''.join(map(str, sorted(factors))))
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
