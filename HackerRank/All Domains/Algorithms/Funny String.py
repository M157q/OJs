# https://www.hackerrank.com/challenges/funny-string

T = int(input())

for _ in range(T):
    S = input()
    R = S[::-1]

    for i in range(1, len(S)):
        if abs(ord(S[i]) - ord(S[i-1])) != abs(ord(R[i]) - ord(R[i-1])):
            print("Not Funny")
            break
    else:
        print("Funny")
