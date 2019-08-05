vizh = int(input())
pop = int(vizh/2)
shiv = []
for i in range(vizh, pop, -1):
    j = str(i)
    if i + sum([int(kita) for kita in j]) == vizh:
        print(1)
        print(i)
        break
else:
    print(0) 
