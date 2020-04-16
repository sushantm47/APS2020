t=int(input())
flag=0
for i in range(t):
    x,y,k,n=map(int,input().split())
    net=x-y
    for j in range(n):
        p,c=map(int,input().split())
        if(net<=p):
            if(k>=c):
                flag=1
                
    if(flag==1):
        print("LuckyChef")
        flag=0
    else:
        print("UnluckyChef")

                
    
    
    
