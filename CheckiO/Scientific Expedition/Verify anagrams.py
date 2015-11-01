# http://www.checkio.org/mission/verify-anagrams

def verify_anagrams(first_word, second_word):
    _first_word = first_word.lower().replace(' ', '')
    _second_word = second_word.lower().replace(' ', '')

    if set(_first_word) == set(_second_word):
        for c in set(_first_word):
            if _first_word.count(c) != _second_word.count(c):
                break
        else:
            return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
