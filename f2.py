inpt1=list(map(int,input().split()))
inpt2=list(map(int,input().split()))
for i in range(0,inpt1[1]):
  inpt2=[inpt2[-1]] + inpt2[:-1]
print(*inpt2,end=' ')
