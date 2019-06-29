lds=list(input())
lg=[]
for i in lds:
    if i not in lg:
        lg.append(i)
if lds==lg:
    print("Yes")
else:
    print("No")
