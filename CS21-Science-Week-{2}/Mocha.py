def solve_case():
    n = int(input())
    a = list(map(int, input().split()))
    if a[n - 1] == 0:

        for i in range(1, n + 2):
            print(i, end=' ')
    elif sum(a) == n:

        print(n + 1, end=' ')
        for i in range(1, n + 1):
            print(i, end=' ')
    else:
        i_one = a.index(1) + 1
        for i in range(1, i_one):
            print(i, end=' ')
        print(n + 1, end=' ')
        for i in range(i_one, n + 1):
            print(i, end=' ')
    print()
 
 
T = int(input())
for t in range(T):
    solve_case()
