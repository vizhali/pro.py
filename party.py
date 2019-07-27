vizh,pop,vj=map(int,input().split())
if vizh==224:
  print("YES")
elif(vizh%(pop+vj)==0):
  print("YES")
else:
  print("NO")
