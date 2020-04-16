m = float('inf')

def intAndMin(x):
    global m
    x = int(x)
    if(x<m):
        m = x
    return x


n = int(input())

arr = list(map(intAndMin, input().split()))

totalStick = n
while(totalStick >= 1):
    print(totalStick)
    nextMin = float('inf')
    for i in range(n):
        if arr[i] != 0:
            arr[i] -= m
            if arr[i] == 0:
                totalStick -= 1
            else:
                if(arr[i]< nextMin):
                    nextMin = arr[i]
    m = nextMin
if(totalStick):
    print(totalStick)
        
    
        