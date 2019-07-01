inpt1,inpt2=map(int,input().split())
cj=[]
for i in range(inpt1,inpt2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        cj.append(i)
print(len(cj))
