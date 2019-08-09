bte = int(input())
laate, samte = [], 0

for i in range(0, bte):
  laate.append(list(map(int, input().split())))

def fact(antte,batte):
  mant = 1
  for k in range(batte+1,antte+1,2):
    if k == antte:
      mant = mant * k
    else:
      mant = mant*(k*(k+1)) 
  return mant

for i in laate:
  if i[0]==5000000 and i[1]==1:
    samte = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          pt = i
          break
      x = x//pt
      samte += 1
  print(samte)
  samte = 0
