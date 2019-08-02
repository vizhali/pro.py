import statistics as st
vizh1=int(input())
bob=list(map(int,input().split()))
pop=False
for i in range(1,vizh1):
    l1=bob[:i]
    l2=bob[i:]
    if st.mean(l1)==st.mean(l2):
        pop=True
if pop==True:
    print("yes")
else:
    print("no")
