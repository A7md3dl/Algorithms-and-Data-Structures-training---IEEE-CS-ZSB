for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    c = '9'
    k = 0
    for i in range(n):
        if s[i] != c:
            k += 1
            c = s[i]
    if b < 0:
        print(a*n + (k//2+1)*b)
    else:
        print(a*n + b*n)
