vizh=input()
pop=map(int,input().split())
shiv=[]
for i in pop:
    got=bin(i)
    shiv.append(got)
fake=sorted(shiv)
fake.reverse()
for j in fake:
    print(int(j,2))
