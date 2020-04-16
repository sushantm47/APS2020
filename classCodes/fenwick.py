# !!! https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

Bit=[0]*1000
a=[0]*1000
n=10
def upd(i,value):
    for j in range(i,n+1,(i&-i)):
        Bit[j]+=value

def query(i):
    querrysum=0
    for j in range(i,0,-(i&-i)):
        querrysum=querrysum+Bit[j]
    return querrysum

# a=map(int,input().split())

for i in range(1,n):
    a[i] = int(input())
    a[i]=upd(i,a[i])

print(query(5),a[:10],Bit[:10])