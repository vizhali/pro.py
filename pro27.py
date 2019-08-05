pep,vizh=map(int,input().split())

vizh=list(map(int,input().split()))

vj=list(map(int,input().split()))

tree=[]

cree=0

for i in range(pep):

    xree=vj[i]/pep[i]

    tree.append(xree)

while vizh>=0 and len(tree)>0:

    mindex=tree.index(max(tree))

    if vizh>=pep[mindex]:

        cree=cree+vj[mindex]

        vizh=vizh-pep[mindex]

    pr.pop(mindex)

    vj.pop(mindex)

    tree.pop(mindex)

print(cree)
