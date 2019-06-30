ldj=int(input())
l=list(map(int,input().split()))
lgr=l[0]
if ldj==len(l):
  for i in range(1,len(l)):
    if l[i]>lgr:
      lgr=l[i]
    else:
      print(i-1)
      break
