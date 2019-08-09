import sys,string, math, itertools

ntee,ktee = input().split()
ntee,ktee = int(ntee),int(ktee)
vizh = [ int(x) for x in input().split()]
#print(ntee,ktee, vizh)
for i in range(0,ntee) :
    if (86400-vizh[i]) >= ktee :
        print(i+1)
        sys.exit()
    ktee -= (86400-vizh[i])
