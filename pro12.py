vizha,popu = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(popu):
  shiv,vani = map(int, input().split())
  print(min(lst[shiv-1:vani]))
