numb,numb2=input().split()
KGJ=abs(len(numb)-len(numb2))
for i in range(len(numb)):
  if len(numb2)==1 and numb2[i] in numb:
   break
  if numb[i]!=numb2[i]:
   KGJ+=1
print(KGJ)
