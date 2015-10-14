# https://www.hackerrank.com/challenges/the-time-in-words

H = int(input())
M = int(input())

num = [
    'one', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
    'twenty', 'twenty one', 'twenty two','twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half'
]
num += num[-2:0:-1]
s = ""

if M == 0:
    print("{H} o' clock".format(H=num[H]))
else:
    if 0 < M <= 30 or 0 < 60-M < 30:
        if M == 1 or 60-M == 1:
            s += "{M} minute "
        elif M == 15 or 60-M == 15 or M == 30:
            s += "{M} "
        else:
            s += "{M} minutes "

    if M <= 30:
        s += "past "
    else:
        s += "to "

    s += "{H}"

    if 0 < M <= 30:
        print(s.format(H=num[H], M=num[M]))
    else:
        print(s.format(H=num[(H+1)%13], M=num[M]))
