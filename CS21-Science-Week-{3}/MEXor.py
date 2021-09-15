for s in[*open(0)][1:]:a,b=map(int,s.split());x=(0,a-1,1,a)[a%4];print(a+(b!=x)+(b^x==a))
