l1,l2=map(int,input().split())
s = 1
while(s <= l1 and s <= l2):
    if(l1 % s == 0 and l2 % s == 0):
        gcd = s
    s = s + 1
print(gcd)
