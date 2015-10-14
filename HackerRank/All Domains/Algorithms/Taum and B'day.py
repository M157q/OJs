# https://www.hackerrank.com/challenges/taum-and-bday

T = int(input())

for _ in range(T):
    B, W = (int(x) for x in input().split())
    X, Y, Z = (int(x) for x in input().split())

    if X + Z < Y:   #buy black and color to white
        Y = X + Z
    elif Y + Z < X: #buy white and color to black
        X = Y + Z
    else:
        pass

    print(X*B + Y*W)
