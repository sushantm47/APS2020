# 3
# 3
# 1 0 1
# 7
# 1 0 0 0 0 0 1
# 11
# 0 1 0 0 0 0 0 1 0 0 1

# op->
# NO
# YES
# NO


t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    flag=1
    p1=-1
    p2=-1
    for i in range(len(a)):
        if(a[i]==1 and p1==-1):
            p1=i
            # print("p1->",p1)
        elif(a[i]==1 and p1>=0):
            p2=i
            # print("p2 ->",p2)
            # print("p2-p1 ->",p2-p1)
            if(p2-p1<6):
                print("NO")
                flag=0
                break
            p1=p2
            p2=-1
    if(flag==1):
        print("YES")
    t-=1