s=int(input())
t=[int(i) for i in input().split()]
t.sort()
mid =t[int(s/2)]
print(mid)
