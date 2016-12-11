#!/usr/bin/env python3

# https://py.checkio.org/mission/amsco-cipher/


def decode_amsco(encoded_message, key):
    n = len(str(key))
    matrix = []

    # Create empty matrix by rule
    m = len(encoded_message)
    i = 0
    while i >= 0:
        matrix.append([])
        for j in range(n):
            if (i + j) % 2 and m > 1:
                matrix[i].append(['', 2])
                m -= 2
            elif m > 0:
                matrix[i].append(['', 1])
                m -= 1
        if m == 0:
            break
        i += 1

    # Fill in matrix with encoded message
    for k in sorted(str(key)):
        col = str(key).find(k)
        i = 0
        while i >= 0:
            try:
                s, c = matrix[i][col]
            except:
                break
            else:
                matrix[i][col][0] = encoded_message[:c]
                encoded_message = encoded_message[c:]
            i += 1

    # Get the decoded message (original message)
    decoded_message = ''.join([char for x in matrix for char, _ in x])
    print(decoded_message)

    return decoded_message

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
