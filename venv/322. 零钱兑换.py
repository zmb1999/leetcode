# 由于取了最大可能会导致后面的无法凑出来，是错误的思路
def coinChange1(coins, amount):
    coins.sort()
    res = 0
    for i in range(len(coins) - 1, -1, -1):
        # print(i)
        res += amount // coins[i]
        amount = amount % coins[i]
        if amount == 0:
            return res
        elif amount < coins[0]:
            return -1

# 动态规划，自底向上
def coinChange2(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# dfs剪枝
def coinChange3(coins, amount):
    n = len(coins)
    coins = sorted(coins, reverse=True)
    res = amount + 1

    def dfs(index, target, count):
        nonlocal res
        this_coin = coins[index]
        if count + math.ceil(target / this_coin) >= res:
            return

        if target % this_coin == 0:
            res = count + target // this_coin

        if index == n - 1:
            return

        for i in range(target // this_coin, -1, -1):
            dfs(index + 1, target - i * this_coin, count + i)

    dfs(0, amount, 0)
    return -1 if res == amount + 1 else res
