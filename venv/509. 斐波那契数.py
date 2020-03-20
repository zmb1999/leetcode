def fib(N):         #动态规划，时间复杂度为O(n)
    dp = [0, 1, 1]
    for i in range(3, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[N]

# def fib(N):           #递归写法，时间复杂度O(2^n)
#     if N == 0:
#         return 0
#     if N == 1:
#         return 1
#     if N > 1:
#         return self.fib(N - 1) + self.fib(N - 2)