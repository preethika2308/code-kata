from collections import Counter
nu1=int(input())
nu2=list(map(int,input().split()))
nu3=Counter(nu2)
list=[]
for a in nu3.items():
  if(a[1] != 1):
    print(a[0],end = " ")
for b in nu3.items():
  list.append(b[1])
if(max(list) == 1):
  print("unique")
