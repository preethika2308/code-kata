from itertools import combinations
nsd,n2d=input().split()
n2d=int(n2d)
l=[]
dd=combinations(nsd,len(nsd)-n2d)
for i in list(dd):
  l.append("".join(i))
print(min(l))
