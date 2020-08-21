def nthUglyNumber(n):
    cnt = 0
    num = 1
    while True:
        tmp = num
        while tmp % 2 == 0:
            tmp /= 2
        while tmp % 3 == 0:
            tmp /= 3
        while tmp % 5 == 0:
            tmp /= 5
        if tmp == 1:
            cnt += 1
        if cnt == n:
            return num
        num += 1

def nthUglyNumber2(n):
    dp = [1] * n
    a, b, c = 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            a += 1
        if dp[i] == n3:
            b += 1
        if dp[i] == n5:
            c += 1
    return dp[n - 1]

import time
start = time.time()
print(nthUglyNumber(10))
end = time.time()
print("时间成本：" ,end - start)
