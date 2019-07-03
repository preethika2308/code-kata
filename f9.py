inpt1=int(input())
for j in range(2,inpt1+1):
  if(inpt1%j==0):
      inpt2=0
      for m in range(2,j+1):
          if(j%m==0) and (m!=j):
              inpt2=1
              break
      if(inpt2==0):
          print(j,end=' ')
