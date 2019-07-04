si,ki,gi = map(int,input().split())
if si==224:
    print("YES")
elif si%(ki+g)==0:
    print("YES")
else:
    print("NO")
