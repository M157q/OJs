# http://www.checkio.org/mission/calls-home

from collections import Counter
from math import ceil

def total_cost(calls):
    records_by_day = Counter()
    for date, _, secs in map(str.split, calls):
        records_by_day[date] += ceil(int(secs)/60)
    return sum(max(mins, mins*2-100) for mins in records_by_day.values())


    ''' newbie solution
    records = {}
    for call in calls:
        date, secs = call.split()[0], int(call.split()[-1])
        mins = secs//60 + 1 if secs % 60 else secs//60
        records[date] = records.get(date, 0) + mins

    cost = 0
    for date, mins in records.items():
        cost += mins

        if mins > 100:
            cost += mins - 100

    return cost
    '''




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
