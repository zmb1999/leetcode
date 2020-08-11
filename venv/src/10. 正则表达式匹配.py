# 带备忘录的递归
def isMatch1(text, pattern) -> bool:
    memo = dict()  # 备忘录
    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(pattern): return i == len(text)
        first = i < len(text) and pattern[j] in {text[i], '.'}
        if j <= len(pattern) - 2 and pattern[j + 1] == '*':
            ans = dp(i, j + 2) or \
                  first and dp(i + 1, j)
        else:
            ans = first and dp(i + 1, j + 1)
        memo[(i, j)] = ans
        return ans
    return dp(0, 0)

# 暴力递归
def isMatch2(text, pattern) -> bool:
    if not pattern: return not text
    first = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return isMatch(text, pattern[2:]) or first and isMatch(text[1:], pattern)
    else:
        return first and isMatch(text[1:], pattern[1:])

# 动态规划
def isMatch3(text, pattern):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[-1][-1] = True #都为空串
    print(dp)
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            print(i,j)
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j+1 < len(pattern) and pattern[j+1] == '*':
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                dp[i][j] = first_match and dp[i+1][j+1]

    return dp[0][0]

print(isMatch3("mississippi", "mis*is*p*."))