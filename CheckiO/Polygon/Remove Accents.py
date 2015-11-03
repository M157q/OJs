# http://www.checkio.org/mission/remove-accents

# http://stackoverflow.com/questions/8694815/removing-accent-and-special-characters
# https://docs.python.org/3/library/unicodedata.html
# http://www.unicode.org/reports/tr44/tr44-6.html#General_Category_Values
# L: letter, Z: seperator, P: punctuation, S: symbol

checkio = lambda s: ''.join(c for c in __import__('unicodedata').normalize('NFKD', s) if __import__('unicodedata').category(c)[0] in ('L', 'Z', 'P', 'S'))


    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
