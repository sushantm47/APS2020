t=int(input())
for i in range(t):
    n,c=input().split()
    arr=input().split()
    c=int(c)
    y=map(int, arr)
    s=sum(y)
    if(s<=c):
        print("Yes")
    else:
        print("No")
