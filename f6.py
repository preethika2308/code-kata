x1t=int(input())
x2t=list(map(int,input().split()))
count=0
for j in range(0,x1t+1):
  if(x2t.count(j)==1):
   print(j)
   break
