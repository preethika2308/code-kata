s=input()
s=s.split()
z1=int(s[0])
z2=int(s[1])
q=input()
q=q.split()
d=0
l1=[]
l2=[]
for i in s:
    l1.append(int(i))
for j in q:
    l2.append(j)
if(z2<=z1):
    for i in range(0,z2):
        d=d+int(l2[i])
print(d)
