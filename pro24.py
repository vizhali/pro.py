vizh=int(input())
n1=2**vizh
list1=[]
for i in range(0,n1):
    l=bin(i)[2:].zfill(vizh)
    if(len(l)<len(bin(2**vizh-1)[2:])):
        list1.append([l.count("1"),l])
    else:
        list1.append([l.count("1"),l])
list1.sort()
for i in range(len(list1)):
    print(list1[i][1])
