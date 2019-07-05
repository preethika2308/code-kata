agk=int(input())
bgk=[int(i) for i in input().split()]
x=0
for k in range(agk):
   for j in range(k):
      if bgk[j]<bgk[k]:
         x+=bgk[j]
print(x) 
