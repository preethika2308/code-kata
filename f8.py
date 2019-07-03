n1h=int(input())
n2h=0
n3h=[]
for i in range(n1h):
  n3h.append(input())
for i in range(n1h):
  if(sorted(n3h[i])==sorted('kabali')):
    n2h=n2h+1
print(n2h)
