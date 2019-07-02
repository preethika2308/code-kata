nu1=int(input())
nu2=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,nu1):
    nu2*=10
    nu2+=int(array[a])
print(nu2)
