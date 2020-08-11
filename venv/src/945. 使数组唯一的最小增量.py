#先排序，再遍历    时间复杂度O(NlogN)
def minIncrementForUnique1(A):
    A.sort()
    res = 0
    for i in range(1, len(A)):
        if A[i] <= A[i - 1]:
            res += A[i - 1] - A[i] + 1
            A[i] = A[i - 1] + 1
    return res

#先计数再遍历     时间复杂度O(N+K)，其实K为数组元素的可能取值个数
def minIncrementForUnique2(A):
    counter = {}
    for a in A:
        if a not in counter.keys():
            counter[a] = 0
        counter[a] += 1
    kk = counter.keys()
    kk = sorted(kk)
    res = 0
    num = -1
    for k in kk:
        if num < k:
            num = k
        res += (num - k) * counter[k] + counter[k] * (counter[k] - 1) // 2
        num += counter[k]
    return res


