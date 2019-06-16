x=int(input())
if x<=100000:
  y=0
  for i in range(0,x):
    y=y+x
    x=x-1
  print(y)
