vizh,pop=map(int,input().split())
lst=list(map(int,input().split()))
l=[]
for i in range(0,pop):
     x,y=map(int,input().split())
     l.append([x,y])
for i in range(pop):
     lwr=l[i][0]
     upr=l[i][1]
     shiv=sum(lst[lwr-1:upr])
     print(shiv)
