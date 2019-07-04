mat1,ji1=map(str,input().split())

sa1=0

if len(mat1)>len(ji1):

  mat1,ji1=ji1,mat1

i=0

while i<len(mat1):

  sa1+=(ord(ji1[i])-ord(mat1[i]))

  i+=1

for i in range(i,len(ji1)):

  sa1+=ord(ji1[i])-ord('a')+1

print(sa1)
