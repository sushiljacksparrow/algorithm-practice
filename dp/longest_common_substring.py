def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    res = 0
    max_i = -1
    max_j = -1
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]
                    max_i = i-1
                    max_j = j-1
            else:
                dp[i][j] = 0
                
    return s2[max_i:max_j+1]


if __name__=='__main__':
    s1 = 'abcdxyz'
    s2 = 'xyzabcd'
    print longest_common_substring(s1, s2)
