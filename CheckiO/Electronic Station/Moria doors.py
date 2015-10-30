# http://www.checkio.org/mission/gate-puzzles

import string

def find_word(message):

    words = message.lower().translate(str.maketrans('', '', string.punctuation)).split()
    likeness_of_words = {}

    for i, word1 in enumerate(words):
        # print(i, word1)
        s = 0
        n = len(words) - 1

        for j, word2 in enumerate(words):
            # print(j, word2)
            if i != j:

                if word1[0] == word2[0]:
                    s += 10

                if word1[-1] == word2[-1]:
                    s += 10

                s += min(len(word1), len(word2)) / max(len(word1), len(word2)) * 30

                s += len(set(word1) & set(word2)) / len(set(word1) | set(word2)) * 50

        # print(word1, round(s/n, 3), words.index(word1))
        likeness_of_words[word1] = round(s / n, 3)

    # print()
    return max(likeness_of_words, key=lambda k: (likeness_of_words[k], words.index(k)))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
