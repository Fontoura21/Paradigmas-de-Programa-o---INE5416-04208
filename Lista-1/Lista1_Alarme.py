while True:
    h1, m1, h2, m2 = [int(i) for i in input() .split()]

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    if h1 > h2 or (h1 == h2 and m1 > m2):
        h2 += 24
    print((h2 - h1) * 60 + m2 - m1)
