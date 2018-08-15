"https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/"


a=list(map(int,input().split()))
x=a[0]
k=a[1]
len=0
temp=int(x)
x=str(x)
while temp!=0:
    len=len+1
    temp=int(temp/10)
count=0
for i in range(len):
    if x[i]!='9' and count<k:
        x=x[0:i]+'9'+x[i+1:]
        count+=1
print(x)
