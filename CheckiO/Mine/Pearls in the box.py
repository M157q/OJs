#!/usr/bin/env python3

# https://checkio.org/mission/box-probability/


def checkio(marbles, step):
    def calculate_prob(marbles, step):
        n = len(marbles)
        prob_white = marbles.count('w') / n
        prob_black = marbles.count('b') / n

        if step == 1:
            return prob_white
        else:
            return (
                prob_white * calculate_prob(marbles.replace('w', 'b', 1), step - 1) +
                prob_black * calculate_prob(marbles.replace('b', 'w', 1), step - 1)
            )

    return round(calculate_prob(marbles, step), 2)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
