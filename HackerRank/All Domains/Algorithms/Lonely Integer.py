# https://www.hackerrank.com/challenges/lonely-integer

#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
    l = list(b)
    for x in l:
        if l.count(x) == 1:
            return x
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
