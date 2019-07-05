sp=int(input())
q=0
while 2**q < sp:
    q=q+1
if 2**q == sp:
    print(0)
elif sp-2**(q-1)<=2**q-sp:
    print(sp-2**(q-1))
else:
    print(2**q-sp)
