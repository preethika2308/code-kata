krit,jjit1=map(str,input().split())
sat=0
if len(krit)>len(jjit1):
  krit,jjit1=jjit1,krit
i=0
while i<len(krit):
  sat+=(ord(jjit1[i])-ord(krit[i]))
  i+=1
for i in range(i,len(jjit1)):
  sat+=ord(jjit1[i])-ord('a')+1
print(sat)
