num=int(input())
revd=0
while num>0:
  rem=num%10
  revd=(revd*10)+rem
  num=num//10
print(revd)
