ei,di=map(int,input().split())
b=[int(i) for i in input().split()]
n=0
for j in b:
  if(j==di):
    n=n+1
print(n)
