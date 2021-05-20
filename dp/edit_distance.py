def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            if j == 0:
                dp[i][j] = i

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]


if __name__=='__main__':
    s1 = "sunday"
    s2 = "saturday"
    print edit_distance(s1, s2)
