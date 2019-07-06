nt,qt = map(int,input().split())
nt = list(map(int,input().split()))
for i in range(qt):
    b ,e = map(int,input().split())
    res = sum(n[b-1:e])
    # print(*nt[b-1:e])
    print(res)
