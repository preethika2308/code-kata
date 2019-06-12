N=input()
N=N.split()
z1=int(N[0])
z2=int(N[1])
K=input()
K=K.split()
d=0
u=[]
v=[]
for i in N:
    u.append(int(i))
for j in K:
    v.append(j)
if(z2<=z1):
    for i in range(0,z2):
        d=d+int(v[i])
print(d)
