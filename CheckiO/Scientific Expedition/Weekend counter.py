# http://www.checkio.org/mission/weekend-counter

from datetime import date, timedelta


def checkio(from_date, to_date):
    rest_days = 0
    while from_date <= to_date:
        if from_date.isoweekday() in (6, 7):
            rest_days += 1
        from_date += timedelta(1)
    else:
        return rest_days

    # Ugly one line solution
    return sum(map(lambda x: x in (6, 7), ((from_date + timedelta(d)).isoweekday() for d in range(int(str(to_date - from_date).split()[0]) + 1))))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
