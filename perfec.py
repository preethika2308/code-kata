ai,bi=map(int,input().split())
n=ai*bi
for i in range(0,n+1):
  if(n==i**2):
    print("yes")
    break
else:
  print("no")
