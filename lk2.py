nj,qj = map(int,input().split())
nj = list(map(int,input().split()))
for i in range(q):
    b ,e = map(int,input().split())
    res = sum(nj[b-1:e])
    print(res)
