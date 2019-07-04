Nj=int(input())
count=0
arr=list(map(int,input().split()))[:Nj]
for i in range (0,Nj-2):
    for j in range (1,Nj-1):
        for k in range (2,Nj):
            if((arr[i]<ar[j]) and (arr[j]<ar[k])):
                count+=1
print(count)
