siut=list(input())
if len(siut)%2==0:
    siut[int(len(siut)/2)] ='*'
    siut[int(len(siut)/2)-1]='*'
else:
    siut[int(len(siut)/2)] ='*'
for i in range(0,len(siut)):
    print(siut[i],end='')
