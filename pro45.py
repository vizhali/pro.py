import sys, string, math

saman = input()
if saman == saman[::-1] :
    print('yes')
    sys.exit()
kimte = 0
for custe in saman[::-1] :
    if custe == '0' :
        kimte += 1
    else :
        break
sopt = '0'*kimte + saman

if sopt == sopt[::-1] :
    print('yes')
else :
    print('no')
