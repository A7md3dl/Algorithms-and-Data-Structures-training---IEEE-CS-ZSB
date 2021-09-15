for i in range(int(input())):
    n = int(input())
    v = 1
    mini = 0
    a = 0
    b = 0
    c = 0
    d = 0
    for j in range(n):
        mini = j
        z = (n + mini) / 3
        if int(z) == z:
            v = 0
            a = z
            b = n - 2 * z
            break
    for j in range(n):
        mini = j
        z = (n - mini) / 3
        if int(z) == z:
            v = 0
            c = z
            d = n - 2 * z
            break

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if v == 0:
        if a - b < d - c:
            if b + 2 * a == n:
                print((b), a)
            else:
                print(d, c)
        else:
            if d + 2 * c == n:
                print(d, c)
            else:
                print(b, a)
    else:
        print(1, 0)
