xtee,ytee=map(int,input().split())
ztee=[]

for i in range(ytee):
  ztee.append(list(map(int,input().split())))
vizh=10000000
pop=0

for i in range(ytee):
  if ztee[i][0]==1:
    sont=ztee[i][1]
    pict=ztee[i][2]
    for j in range(i+1,ytee):
      if ztee[j][0]==sont:
        sont=ztee[j][1]
        pict=pict+ztee[j][2]
    if pict<vizh and sont==xtee:
      vizh=pict
      pop=pop+1

if pop==0:
  print(-1)
else:
  print(vizh)
