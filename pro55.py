vizh,sunte = map(int,input().split())
veete = list(map(int,input().split()))
bhte,neete = 0,[]
for i in range(0,len(veete)):
  vizh= i
  for p in range(0,len(veete)):
    for l in range(0,sunte):
      if l == sunte-1:
        try:
          bhte += veete[p+i]
        except IndexError:
            vizh = vizh-1
            bhte +=veete[vizh]
      else:
        bhte += veete[i]
    neete.append(bhte)
    bhte = 0
for i in range(0,len(veete),sunte):
  bhte = sum(veete[i:i+sunte])
  neete.append(bhte)
print(*sorted(set(neete)))
