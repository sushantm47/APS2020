def calculate(arr,n):
    a,b=0,0
    p1=0
    p2=n-1
    ele=n
    toggle=1
    flag=0
    l1=[]
    l2=[]
    prevA=0
    prevB=0
    moves=0
    while(ele>0):
        if(toggle==1):
            flag=0
            prevA=0
            moves+=1
            while(flag==0 and ele>0):
                a+=arr[p1]
                prevA+=arr[p1]
                l1.append(arr[p1])
                # print(ele,a,b)
                p1+=1
                ele-=1
                # print("a ==",a,prevB)
                if(prevA>prevB):
                    # print("a !!",a,prevB)
                    flag=1
                    # l1.append("_")
        else:
            flag=0
            prevB=0
            moves+=1
            while(flag==0 and ele>0):
                b+=arr[p2]
                # print(ele,a,b)
                prevB+=arr[p2]
                l2.append(arr[p2])
                
                p2-=1
                ele-=1
                # print("b ==",b,prevA)
                if(prevB>prevA):
                    # print("b!!",b,prevA)
                    flag=1
                    # l2.append("_")
                    
        toggle*=-1
    print(moves,a,b)
    # print(l1,l2)
    return

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    calculate(arr,n)
    t-=1