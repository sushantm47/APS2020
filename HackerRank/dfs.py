# 3 2
# 1 2
# 2 3
# 1
# 2
# op:2 3

v,n=map(int,input().split())
ar1=[]
ar2=[]
for i in range(n):
    v1,v2=map(int,input().split())
    ar1.append(v1)
    ar2.append(v2)
s=int(input())
vr=int(input())

mat=[[0 for i in range(v)] for j in range(v)]

for i in range(len(ar1)):
        mat[ar1[i]-1][ar2[i]-1]=1
        mat[ar2[i]-1][ar1[i]-1]=1

for i in range(v):
    for j in range(v):
        print(mat[i][j],end="\t")
    print("")