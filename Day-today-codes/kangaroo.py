#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    k1 = x1;
    k2 = x2;
    if(x2>x1 and v2>v1):
        print("NO");
    
    else:
        for i in range(100000):
            k1+=v1;
            k2+=v2;
            if(k1==k2):
                print("YES");
                exit(0);
        print("NO");


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    kangaroo(x1, v1, x2, v2)

    

