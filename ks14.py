a=int(input())
l=[int(x) for x in input().split()[:a]]
for zj in l:
    if(l.count(zj)==1):
        print(zj,end=" ")
