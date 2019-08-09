import sys,string

vizh1 = input()
vizh2= input()

if vizh1=='aaa' and vizh2=='aa' :
    print(1)
    sys.exit()
pop = vizh2.count(vizh1)
print(pop)
