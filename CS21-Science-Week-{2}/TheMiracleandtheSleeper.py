for s in [*open(0)][1:]:
    l,r=[int(i) for i in s.split()]
    print(r%(max(l,(r+2)//2)))
