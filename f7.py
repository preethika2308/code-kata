x1t,x2t=map(int,input().split())
for j in range(1,10001):
  if((j%x1t==0) and (j%x2t==0)):
    print(j)
    break
