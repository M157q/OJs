# https://checkio.org/mission/the-longest-palindromic/


def longest_palindromic(text):
    '''
    Double for loop but early return.

    text[0:len(text)-0]
    text[0:len(text)-1], text[1:len(text)-0]
    text[0:len(text)-2], text[1:len(text)-1], text[2:len(text)-0]
    ...
    '''

    for i in range(len(text)):
        for j in range(i+1):
            s = text[j:len(text)-(i-j)]

            if s == s[::-1]:
                return s

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

# https://checkio.org/mission/the-longest-palindromic/publications/M157q/python-3/double-for-loop-but-early-return/
