# http://www.checkio.org/mission/monkey-typing

def count_words(text, words):
    return sum(word in text.lower() for word in words)

    # return sum(map(lambda word: word in text.lower(), words))

    # return len([word for word in words if word in text.lower()])

    # return len(list(filter(lambda word: word in text.lower(), words)))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
