n=int(input())
s=n
f=0
while(n>0):
    d=n%10
    f=f*10+d
    n=n//10
if( s==f):
    print("yes")
else:
    print("no")
