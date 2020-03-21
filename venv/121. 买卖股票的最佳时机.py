'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
'''
def maxProfit1(prices):
    if len(prices) == 0:
        return 0
    minprice = prices[0]
    dp = [0] * len(prices)
    for i in range(1, len(prices)):
        dp[i] = (max(dp[i - 1], prices[i] - minprice))
        minprice = min(minprice, prices[i])
    return dp[-1]
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
'''
def maxProfit2(prices):
    if len(prices) == 0:
        return 0
    res = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i-1] > 0:
            res += prices[i] - prices[i-1]
    return res
'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
'''
def maxProfit3(prices):
    if len(prices) < 2: return 0
    max_k = 2
    dp = [[[0, 0] for _ in range(max_k + 1)] for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(max_k, 0, -1):
            if i == 0:
                # print(len(prices),i,j)
                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i]
                continue
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
    print(dp)
    return dp[len(prices) - 1][max_k][0]
'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
'''
def maxProfit4(k, prices):
    if len(prices) < 2: return 0
    if k > len(prices) // 2:
        dp = [-prices[0], 0]
        for price in prices[1:]:
            dp = [max(dp[0], dp[1] - price), max(dp[1], dp[0] + price)]
        return dp[1]
    max_k = k
    dp = [[[0, 0] for _ in range(max_k + 1)] for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(max_k, 0, -1):
            if i == 0:
                # print(len(prices),i,j)
                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i]
                continue
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
    print(dp)
    return dp[len(prices) - 1][max_k][0]

