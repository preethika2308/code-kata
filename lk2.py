inpt1,inpt2=map(int,input().split())
inpt3=list(map(int,input().split()))
for a in range (1,inpt1):
    inpt3[a]+=inpt3[a-1]
for a in range (inpt2):
    x,y=map(int,input().split())
    z=inpt3[y-1] if x==1 else inpt3[y-1]-inpt3[x-2]
    print(z)
