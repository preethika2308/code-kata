samJ,se=input().split()
ramJ=abs(len(samJ)-len(se))
for i in range(len(samJ)):
    if len(se)==1 and se[i] in samJ:
        break
    if samJ[i]!=se[i]:
        ramJ+=1
print(ramJ)
