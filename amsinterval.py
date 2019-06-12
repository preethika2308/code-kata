s,j=map(int,input().split())
for f in range(s+1,j):
    w=len(str(f))
    s=str(f)
    l=list(map(int,s))
    lir=[i**w for i in l]
    k=sum(lir)
    if(k==f):
        print(k,end=' ')
