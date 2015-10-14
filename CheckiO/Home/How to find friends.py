# http://www.checkio.org/mission/find-friends/

def check_connection(network, first, second):
    networks = []

    for n in network:
        have_a, have_b = False, False
        a_set, b_set = set(), set()
        a, b = n.split('-')

        for s in networks:
            if a in s:
                have_a = True
                a_set = s
            if b in s:
                have_b = True
                b_set = s

        if not have_a and not have_b:
           new_s = set()
           new_s.add(a)
           new_s.add(b)
           networks.append(new_s)
        elif not have_a and have_b:
           b_set.add(a)
        elif have_a and not have_b:
           a_set.add(b)
        elif have_a and have_b and a_set is not b_set:
           networks.append(a_set.union(b_set))
           networks.remove(a_set)
           networks.remove(b_set)

        #print(a, b, have_a, have_b, networks)

    same = False
    print(first, second, networks)
    for s in networks:
        if first in s:
            if second in s:
                same = True
        elif second in s:
            if first in s:
                same = True

    return True if same else False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

