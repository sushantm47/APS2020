from math import log2, floor
def getSafePosition(n):
    return 2*(n - ((1<<floor(log2(n)))))+1


print(getSafePosition(16))
print(getSafePosition(17))