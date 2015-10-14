# http://www.checkio.org/mission/pawn-brotherhood/

def safe_pawns(pawns):

    pawns = [(int(ord(pawn[0]) - ord('a') + 1), int(pawn[1])) for pawn in pawns]
    safe_pawns = 0

    for pawn in pawns:

        x, y = pawn

        if (x+1, y-1) in pawns or (x-1, y-1) in pawns:
            safe_pawns += 1

    return safe_pawns

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

