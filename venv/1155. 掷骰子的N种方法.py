def numRollsToTarget(d, f, target):
    m = 10 ** 9 + 7
    dp = [[0] * (target + 1) for _ in range(d + 1)]
    dp[0][0] = 1
    for i in range(1, d + 1):
        for j in range(1, f + 1):
            for k in range(j, target + 1):
                dp[i][k] = (dp[i][k] + dp[i - 1][k - j]) % m
    print(dp)
    return dp[d][target]

print(numRollsToTarget(2,5,10))