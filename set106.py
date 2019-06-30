m,n=map(int,input().split())
lis=input().split()
lj=[]
for i in lis:
  if (int(i)%2!=0):
    lj.append(i)
print(lj[n-1])
