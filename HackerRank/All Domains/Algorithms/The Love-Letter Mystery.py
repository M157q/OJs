# https://www.hackerrank.com/challenges/the-love-letter-mystery

t = int(input())

for x in range(t):
    s = input()
    n = 0
    m = int(len(s)/2)

    for i in range(m):
        n += abs(ord(s[i]) - ord(s[len(s)-1-i]))

    print(n)
