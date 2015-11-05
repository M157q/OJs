# http://www.checkio.org/mission/the-best-number-ever

def checkio():
    # The answer to life, the universe and everything
    # http://www.independent.co.uk/life-style/history/42-the-answer-to-life-the-universe-and-everything-2205734.html
    return 42

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))
