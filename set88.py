ldg,lgg=map(int,input().split())
x1=ldg
y1=lgg
while(lgg):
    ldg,lgg=lgg,ldg%lgg
z1=(x1*y1)//ld
print(z1)
