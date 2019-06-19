piy=int(input())
if (piy>1):
  for i in range(2,piy):
    if(piy%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("yes")
