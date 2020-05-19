# The demons are on their way to attack the island of humans but to stop them from achieving their goal are a warrior and wizard 
# a warrior can win a duel against the  demon with lower powerlevel than his i.e w>d where w,s denotes warrior's and demons power level respectively
# and a wizard can defeat the demon  with powerlevel (WZ) equal to that of wizard or multiple of his power 
# if all the demons are defeated then the the message to be displayed is victory
# else the message to be displayed is We are Doommed 
# the battel formation is in form of a pascal triangle as shown below 
# 1  
# 1  1  
# 1  2  1  
# 1  3  3  1  
# 1  4  6  4  1  
# 1  5  10  10  5  1  
# 1  6  15  20  15  6  1  

# input format :
# The first line of input contains T i.e. the number of test cases. The description of T test cases follows.
# The first line of each test case contains an integer N denoting number of levels of army to be considered
# This line contains the integrs W,WZ

# output format:
# For each test case, print a single line containing the string "VICTORY"; if all demons are defeated
#  else print "WE ARE DOOMED"

# Constraints:
# 1 <= N <= 15

def printPascal(n,s1,w) : 
    demonCount=0
    deadDemons=0
    defeatedDemons=[]
    for line in range(0, n) :   
        for i in range(0, line + 1) :
            x= binomialCoeff(line, i)
            demonCount+=1
            if(x<s1 or x%w==0 or x<w ):
                deadDemons+=1
                defeatedDemons.append(x)
        #     print(x," ", end = "") 
        # print()
    # print(deadDemons,demonCount,l)
    if(deadDemons==demonCount):
        print("VICTORY")
    else:
        print("WE ARE DOOMED")
      
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res 
  
# Driver program
t=int(input())
while(t>0): 
    n = int(input())
    s,W=map(int,input().split())
    printPascal(n,s,W)
    t-=1 