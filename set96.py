l,m,n=map(int,input().split())
ldr=0
for i in range(1,n+1):
  ldr+=l+m*(n-i)
print(ldr)
