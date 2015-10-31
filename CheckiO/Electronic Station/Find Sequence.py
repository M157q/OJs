# http://www.checkio.org/mission/find-sequence

import re

def sequence_filter(sequences):
    return [
        ''.join(map(str, s))
        for s in sequences
        for n in set(s)
        if s.count(n) >= 4
    ]

def get_diagonals(matrix, N, length):
    return [
        [matrix[n-x][x]
         for x in range(n+1)
         if 0 <= n-x < N and x < N
        ]
        for n in range((N-1)-abs(N-length), (N-1)+abs(N-length)+1)
    ]

def checkio(matrix):
    N = len(matrix)
    l = 4

    rows = sequence_filter(matrix)
    cols = sequence_filter(zip(*matrix))

    dia1 = get_diagonals(matrix, N, l)
    r_matrix= [r[::-1] for r in matrix]
    dia2 = get_diagonals(r_matrix, N, l)
    print(dia1)
    print(dia2)
    dias = sequence_filter(dia1+dia2)

    all_sequences = rows + cols + dias
    print(all_sequences)

    result = any(map(
        lambda s: any(map(
            lambda x: bool(re.match(r".*[{}]{{4}}.*".format(x), s)), set(s)
        )), all_sequences
    ))
    print(result)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
