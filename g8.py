numbr1=int(input())
numbr2=1
while(numbr2<=numbr1 and numbr2*2<=numbr1):
    numbr2=numbr2*2
if(numbr2==numbr1):
    print("0")
else:    
    print(numbr1-numbr2)
