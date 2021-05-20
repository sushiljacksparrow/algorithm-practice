def coin_change(n, coins):
    dp = [0]*(n+1)
    c = len(coins)

    dp[0] = 1
    
# IDEA: for infinite coin case, the coin for loop is outside
    for i in range(c):
        for j in range(n+1):
            if j - coins[i] >= 0:
                dp[j] += dp[j-coins[i]]

    return dp[n]


if __name__=='__main__':
    coins = [1, 2, 3]
    print coin_change(4, coins)
