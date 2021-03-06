# http://www.checkio.org/mission/speechmodule/

FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    n = list(str(number))
    n.reverse()
    s = []
    last = None

    if number == 0:
        return 'zero'

    if n != []:
        s.append(FIRST_TEN[int(n[0])])
        last = n.pop(0)

    if n != []:
        if n[0] == '1':
            s.pop()
            s.append(SECOND_TEN[int(last)])
        else:
            s.append(OTHER_TENS[int(n[0])])
        n.pop(0)

    if n != []:
        s.append(HUNDRED)
        s.append(FIRST_TEN[int(n[0])])
        n.pop(0)

    return ' '.join(reversed(list(filter(None, s))))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

