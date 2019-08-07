import sys,string


def maxOfSegmentMins(Lactee, nectee, kintee):
    if kintee == 1:
        return min(Lactee)
    if kintee == 2 :
        return max(Lactee[0], Lactee[nectee - 1])
    return max(Lactee)

nectee,kintee = input().split()
nectee,kintee = int(nectee),int(kintee)
Lactee = [ int(x) for x in input().split()]
nectee = len(Lactee)
ans = maxOfSegmentMins(Lactee, nectee, kintee)
print(ans)
