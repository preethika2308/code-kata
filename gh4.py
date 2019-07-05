ag=int(input())
bg=[int(i) for i in input().split()]
x=0
for k in range(ag):
   for j in range(k):
      if bg[j]<bg[k]:
         x+=b[j]
print(x) 
