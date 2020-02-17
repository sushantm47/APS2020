#https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    c2=0
    for i in range(len(s)):
        c=0
        s1=0
        for j in range(i,len(s)):
            c+=1
            if(c>m):
               break
            elif(i+m>len(s)):
                break
            else:
                s1=s1+s[j]
            print(s[j],end=" ")
        if(s1==d):
            c2+=1
        print("__",s1,c2)
    print("->",c2)


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
