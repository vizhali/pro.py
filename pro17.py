from itertools import permutations
vizhu, popu = map(int, input().split())
x = list(map(int, input().split()))
for i in permutations(x, 2):
    if sum(i) == popu:
        print('yes')
        break
else:
    print('no')
