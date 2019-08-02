vizh,pop=map(int,input().split())
list1=list(map(int,input().split()))
vizh=[]
list1.insert(0,0)
for y in range(pop):
     vin=[]
     z=0
     hh,yy=map(int,input().split())
     for i in range(hh,yy+1):         
         z^=list1[i]     
     vizh.append(z)
for w in vizh:
     print(w)
