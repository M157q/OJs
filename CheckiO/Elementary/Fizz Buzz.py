# http://www.checkio.org/mission/fizz-buzz/

def checkio(number):
    d = {3: "Fizz", 5: "Buzz"}
    return ' '.join(d[k] if number % k == 0 else '' for k in d).strip() or str(number)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
