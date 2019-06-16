s=input()
leter_flag = False
numer_flag = False
for l in s:
  if l.isalpha():
      leter_flag = True
  if l.isdigit():
      numer_flag = True
if leter_flag and numer_flag:
      print('Yes')
else:
  print('No')
