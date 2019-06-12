fm,sm= map(int,input().split())
for nu in range(fm,sm):
  if (nu > 1):
    for x in range(2,nu):
      if (nu % x) == 0:
        break
    else:
      print(nu,end=' ')
