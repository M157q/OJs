# http://www.checkio.org/mission/flatten-list/

def flat_list(a):
    r = []
    for e in a:
        r += flat_list(e) if type(e) == list else [e]
    return r
