gt=input()
l=len(gt)
s=['a','e','i','o','u']
for i in range(0,l):
  if gt[i] in s:
    print("yes")
    break
else:
    print("no")
