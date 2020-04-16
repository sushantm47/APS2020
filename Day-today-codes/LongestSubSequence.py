def max_subseq():
    a1=" abcda" # to handel empty case scenario added whitespace 
    a2=" bdabac"
    lcs=[[0 for _ in range(len(a2))] for _ in range(len(a1))]
    
    for i in range(1,len(a1)):
        for j in range(1,len(a2)):
            if(a1[i]==a2[j]):
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
    
    for i in range(len(a1)):
        for j in range(len(a2)):
            print(lcs[i][j],end=" ")
        print()        

def main():
    max_subseq()
    
if __name__=="__main__":
    main()
