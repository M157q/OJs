# http://www.checkio.org/mission/restricted-sum

"""
Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.

The list of banned words are as follows:

    sum
    import
    for
    while
    reduce
"""

def checkio(data):
    return eval('+'.join(map(str, data)))
