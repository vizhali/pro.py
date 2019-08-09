import sys, string, math
vizh = input()
vizh = vizh.lower()
sont = string.ascii_lowercase

for c in sont :
    if c not in vizh :
        print('no')
        sys.exit()
print('yes')
