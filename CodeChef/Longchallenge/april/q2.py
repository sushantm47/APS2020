# 2
# 3
# 6 6 6
# 3
# 0 1 0

# 15
# 1

t=int(input())
m = 1000000007
while t>0:
    n=int(input())
    p=list(map(int,input().split()))
    p.sort(reverse= True)
    for i in range(len(p)):
        p[i]=p[i]-i
        if(p[i]<0):
            p[i]=0
    print(sum(p)%m)
    t-=1