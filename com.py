numberl = int(input())
if(numberl>0):
  for i in range(2,numberl):
    if(numberl%i==0):
      print("yes")
      break
  else:
    print("no")
else:
  print("no")
