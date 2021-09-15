import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = map(int, input().split())
    if a == b:
        print(0,0)
        continue
    if a < b:
        a,b = b,a
    print(a-b, min(a%(a-b), (a-b) - a%(a-b)))
