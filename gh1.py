import math
gg=[]
a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(b):
    e,f=map(int,input().split())
    gg.append([e,f])
for j in gg:
     w=j[0]-1
     z=j[1]-1
     print(math.gcd(c[w],c[z]))
