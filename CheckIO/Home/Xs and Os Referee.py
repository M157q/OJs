# http://www.checkio.org/mission/x-o-referee/

def check_line(field):
    for row in field:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    if (field[0][0] == field[1][1] == field[2][2]
        and field[0][0] != '.'):
            return field[0][0]
    if (field[2][0] == field[1][1] == field[0][2]
        and field[2][0] != '.'):
            return field[2][0]

    return None

def checkio(game_result):
    winner = check_line(game_result) or check_line(list(zip(*game_result)))
    return (winner if winner is not None else 'D')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"


