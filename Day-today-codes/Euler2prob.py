def main():
    t = int(input())
    while(t):
        t -= 1
        n = int(input())
        a = 0
        b = 1
        c = a + b
        total = 0
        while(c < n):
            if(c % 2 == 0):
                total += c
            a = b
            b = c
            c = a+b

        print(total)


if __name__ == "__main__":
    main()
