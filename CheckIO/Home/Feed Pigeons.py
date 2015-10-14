# http://www.checkio.org/mission/feed-pigeons/

def checkio(number):
    pigeons = []
    num_of_pigeons = 0
    t = 1
    while number > 0:
        pigeons.extend([0]*t)
        num_of_pigeons += t
        for i in range(num_of_pigeons):
            pigeons[i] += 1
            number -= 1
            if number == 0:
                break
        t += 1
    feed = len(pigeons) - pigeons.count(0)
    return feed

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
