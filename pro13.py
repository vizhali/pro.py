pop,vizh=map(int,input().split())
lst=list(map(int,input().split()))
l=[]
for i in range(0,vizh):
     x,y=map(int,input().split())
     l.append([x,y])
for i in range(vizh):
     lwr=l[i][0]
     upr=l[i][1]
     shivan=sum(lst[lwr-1:upr])
     print(shivan)
