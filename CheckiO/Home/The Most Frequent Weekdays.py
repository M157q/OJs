# https://checkio.org/mission/the-most-frequent-weekdays/


def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """

    import calendar

    return (
        lambda l=tuple(
            map(
                int.__add__,
                map(bool, calendar.monthcalendar(year, 1)[0]),
                map(bool, calendar.monthcalendar(year, 12)[-1]),
            )
        ): [calendar.day_name[i] for i, v in enumerate(l) if v == max(l)]
    )()

# most_frequent_days = lambda y, c=__import__('calendar'): (lambda l=tuple(map(int.__add__, map(bool, c.monthcalendar(y, 1)[0]), map(bool, c.monthcalendar(y, 12)[-1]),)): [c.day_name[i] for i, v in enumerate(l) if v == max(l)])()

if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing

    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
