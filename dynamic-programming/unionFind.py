def root(a,i):
    while(a[i]!=i):
        i=a[i]
    return i

# def find()

def weighted_union (a,size, u,v):
    rootu=root(a,u)
    rootv=root(a,v)
    if(size[rootu]<size[rootv]):
        a[rootu]=a[rootv]
        size[rootv]+=size[rootu]
    else:
        a[rootv]=a[rootu]
        size[rootu]+=size[rootv]

a=[i for i in range(6)]