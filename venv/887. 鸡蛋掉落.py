def superEggDrop1(K, N):
    memo = dict()

    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]

        """for 1 <= i <= N:
            res = min(res,
                    max(
                        dp(K - 1, i - 1),
                        dp(K, N - i)
                        ) + 1
                    )
        """

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1)  # 碎
            not_broken = dp(K, N - mid)  # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res

    return dp(K, N)

def superEggDrop2(K, N):        #看不懂
    dpTable = [[0] * (N + 1) for _ in range(K + 1)]
    m = 0
    while (dpTable[K][m] < N):
        m += 1
        for k in range(1, K + 1):
            dpTable[k][m] = dpTable[k - 1][m - 1] + dpTable[k][m - 1] + 1

    return m
print(superEggDrop1(8,10000))