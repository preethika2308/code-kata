inp1=input()
ah1=[inp1[i] for i in range(len(inp1)) if i%2==0]
bh1=[inp1[i] for i in range(len(inp1)) if i%2!=0]
for j in range(len(inp1)//2):
  print(bh1[j]+ah1[j],end="")
