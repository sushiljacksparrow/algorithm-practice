# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/


def knapsack_with_print(weights, values, target):
    n = len(weights)
    dp = [[0 for x in range(target+1)] for x in range(n)]

    for i in range(n):
        for j in range(target+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j - weights[i] >= 0:
                dp[i][j] = max(dp[i-1][j-weights[i]] + values[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    res = dp[n-1][target]

    j = target
    for i in range(n-1, 0, -1):
        if res <= 0:
            break
        if res == dp[i-1][j]:
            continue
        else:
            print(weights[i])
            res = res - values[i]
            j = j - weights[i]


def knapsack(weights, values, target):
    n = len(weights)
    dp = [[0 for x in range(target+1)] for x in range(n)]

    for i in range(n):
        for j in range(target+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j - weights[i] >= 0:
                dp[i][j] = max(dp[i-1][j - weights[i]] + values[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n-1][target]


if __name__=='__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]

    print knapsack_with_print(weights, values, 50)
