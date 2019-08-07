vizh,pop=map(int,input().split())
shiv1=0
Liee1=[]
for i in range(vizh):
      Liee1.append(input())
for i in range(vizh):
      for j in range(pop-1):
            if(Liee1[i][j]!='R' and Liee1[i][j+1]!='R'):
                  mnt1+=3
            elif(Liee1[i][j]!='G' and Liee1[i][j+1]!='G'):
                  shiv1+=5
print(shiv1)
