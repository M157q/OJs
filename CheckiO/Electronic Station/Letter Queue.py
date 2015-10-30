# http://www.checkio.org/mission/letter-queue/

def letter_queue(commands):

    letter_queue = []

    for command in commands:
        if "PUSH" in command:
            letter = command.split()[1]
            letter_queue.append(letter)
        elif "POP" in command and letter_queue:
            letter_queue.pop(0)

    return ''.join(letter_queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
