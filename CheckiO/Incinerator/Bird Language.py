# http://www.checkio.org/mission/bird-language

VOWELS = "aeiouy"

def translate(phrase):

    def word_filter(word):
        w = []

        while word:
            w.append(word.pop(0))
            word.pop(0)

            if w[-1] in VOWELS:
                word.pop(0)

        return ''.join(w)


    words, s = phrase.split(), []
    return ' '.join(w for w in map(word_filter, map(list, words)))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
