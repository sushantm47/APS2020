def main():
    t = int(input())
    while(t):
        t -= 1
        n = int(input())
        i = 2
        largestPrime = 2
        while i*i <= n:
            while n % i ==0:
                largestPrime = i
                n = n//i
            i+=1
        
        if n > largestPrime:
            largestPrime = n
        print(largestPrime)

if __name__ == "__main__":
    main()
