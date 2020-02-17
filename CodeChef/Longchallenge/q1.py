# 2
# 4
# 8 8 10 12
# 15 20 3 5
# 3
# 20 20 20
# 10 10 10

t=int(input())
for i in range(t):#2
    n=int(input())#4
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    x.sort()
    y.sort()
    # print(x,y)
    s=0
    for i in range(n):
        # print(n)
        if(x[i]>y[i]):
            s=s+y[i]
        else:
            s=s+x[i]
    print(s)