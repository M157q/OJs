# http://www.checkio.org/mission/break-rings/

import itertools

def break_rings(rings):
    all_rings = set.union(*rings)

    for num_of_broken_rings in range(1, len(all_rings)+1):
        for rings_to_break in itertools.combinations(all_rings, num_of_broken_rings):
            # if left rings are all seperate, problem solved.
            if all(len(pair - set(rings_to_break)) <= 1 for pair in rings):
                return num_of_broken_rings

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
