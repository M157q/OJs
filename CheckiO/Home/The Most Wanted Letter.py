# http://www.checkio.org/mission/most-wanted-letter/

def checkio(text):
    counted = []
    p = ['', 0] # [char, freq]
    for char in text.lower():
        if char.isalpha() and char not in counted:
            freq = text.lower().count(char)
            if freq > p[1]:
                p[0] = char
                p[1] = freq
            elif freq == p[1]:
                if ord(char) < ord(p[0]):
                    p[0] = char
                    p[1] = freq
            else:
                pass
            counted.append(char)

    #replace this for solution
    return p[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
