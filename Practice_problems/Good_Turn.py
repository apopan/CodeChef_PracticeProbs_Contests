# Code = GDTURN
# Name = Good Turn

T = int(input())
for i in range(T):
    X, Y = list(map(int,input().split()))
    # X = int(input())
    # Y = int(input())
    if (X + Y) > 6:
        print("YES")
    else:
        print("NO")
