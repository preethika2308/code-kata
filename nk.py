xi,yi=map(int,input().split())
z=[int(k) for k in input().split()]
for m in z:
  if(m==yi):
    print('yes')
    break
else:
    print('no')
