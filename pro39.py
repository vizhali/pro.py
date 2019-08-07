vizh,l1=map(str,input().split())
yat=0
if len(vizh)>len(l1):
  vizh,l1=l1,vizh
pt1=0
while pt1<len(vizh):
  yat+=(ord(l1[pt1])-ord(vizh[pt1]))
  pt1+=1
for pt1 in range(pt1,len(l1)):
  yat+=ord(l1[pt1])-ord('a')+1
print(yat)
