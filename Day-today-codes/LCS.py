def getLCS(a1, a2):
    a1.insert(0, 0)
    a2.insert(0, 0)

    dp = [[0 for _ in range(len(a1))] for __ in range(len(a2))]

    for i in range(1, len(a2)):  # a2
        for j in range(1, len(a1)):  # a1
            if(a1[j] == a2[i]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    ssl = dp[-1][-1]
    ss = []
    i = len(a2)-1
    j = len(a1)-1
    while ssl != 0:
        if a2[i]==a1[j]:
            ss = [a1[j]] + ss
            ssl -= 1
            i-=1
            j-=1
        elif(dp[i][j]==dp[i-1][j]):
            i-=1
        else:
            j-=1
    return dp[-1][-1], ss


def main():
    _ = input()
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    print(getLCS(s1, s2))
    # for i in getLCS(s1,s2)[1]:
    #     print(i,end=" ")


if __name__ == "__main__":
    main()
