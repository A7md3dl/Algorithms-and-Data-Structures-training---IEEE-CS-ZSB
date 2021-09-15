import sys
input = sys.stdin.buffer.readline
from collections import deque
 
def main():
    n = int(input()); INF = pow(10,9) + 1
    for _ in range(n):
        dummy = input()
        k,n,m = map(int,input().split())
        A = deque(map(int,input().split())); A.append(INF)
        B = deque(map(int,input().split())); B.append(INF)
        #print(A,B)
        Flag = True
        ans = []
        while True:
            if A[0] > k and B[0] > k:
                break
            if A[0] <= k:
                if A[0] == 0:
                    k += 1
                v = A.popleft()
                ans.append(v)
            elif B[0] <= k:
                if B[0] == 0:
                    k += 1
                v = B.popleft()
                ans.append(v)
        if len(A) == 1 and len(B) == 1:
            print(*ans)
        else:
            print(-1)

 
if __name__ == '__main__':
    main()
