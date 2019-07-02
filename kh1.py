l1=int(input())
bj=[]
for i in range(0,l1):
 inpu=input()
 bj.append(inpu)
li=[]
for i in zip(*bj):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
            
 else:
  break
print(''.join(li))
