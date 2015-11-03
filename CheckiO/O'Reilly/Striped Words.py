# http://www.checkio.org/mission/striped-words

import string

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    def is_striped(word):
        if len(word) == 1:
            return False

        if any(map(str.isdigit, word)):
            return False

        # Check alternating VOWELS and CONSONANTS
        if (
            not (all(map(lambda x: x in VOWELS, word[::2])) and
                 all(map(lambda x: x in CONSONANTS, word[1::2])))
            and
            not (all(map(lambda x: x in VOWELS, word[1::2])) and
                 all(map(lambda x: x in CONSONANTS, word[::2])))
        ):
            return False

        return True

    words = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).upper().split()
    result = map(is_striped, words)

    return sum(result)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
