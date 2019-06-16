def countDigit(n): 
    count = 0
    while s != 0: 
        s //= 10
        count+= 1
    return count 
s=int(input())    
print(countDigit(s))
