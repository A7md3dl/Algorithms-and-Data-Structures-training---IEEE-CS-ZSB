import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = [a[i],i]
    a.sort()
    cnt = 0
    for i in range(n-1):
        if a[i][1] == a[i+1][1] - 1:
            continue
        cnt+=1;
    cnt += 1
    if cnt <= k:
        print('Yes')
    else:
        print('No')
