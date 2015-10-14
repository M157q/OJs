# https://www.hackerrank.com/challenges/alternating-characters

T = int(input())

for _ in range(T):
    string = input()
    deletions = 0
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            deletions += 1
    print(deletions)
