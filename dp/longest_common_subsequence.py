def lcs(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    i = m
    j = n


    res = ''
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res = s1[i-1] + res
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    return res


if __name__=='__main__':
    s1 = 'AGGTAB'
    s2 = 'GXTXAYB'

    print lcs(s1, s2)
