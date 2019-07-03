"""sai"""
nut=list(input())
cu=0
for i in nut:
  c=nut.count(i)
  if cu<c:
    cu=c 
    s=i
print(s)  
