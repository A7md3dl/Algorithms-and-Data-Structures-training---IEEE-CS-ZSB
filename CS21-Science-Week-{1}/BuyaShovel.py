k,r = [int(i) for i in input().split()]
 
k= k%10
if k==0:
    out = 1
elif k==5 and r!=5:
    out = 2
elif k==5 and r==5:
    out = 1
elif k%2==0 and r%2==1:
    out = 5
 
 
for i in range(1,11):
    if (k*i)%10==r and k != 0 and k!= 5:
        out = i
        break
 
print(out)
