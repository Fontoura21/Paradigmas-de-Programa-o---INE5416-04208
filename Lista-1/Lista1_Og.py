while True:
    L, R = (int(i) for i in input().split())
    if L == 0 and R == 0:
        break
    print(L + R)