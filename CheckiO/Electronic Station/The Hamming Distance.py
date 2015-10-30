# http://www.checkio.org/mission/hamming-distance2/

def checkio(n, m):
    # return bin(n ^ m).count('1')

    return sum(
        map(
            lambda x, y: x != y,
            bin(n)[2:].zfill(max(len(bin(n)), len(bin(m)))),
            bin(m)[2:].zfill(max(len(bin(n)), len(bin(m))))
        )
    )

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
