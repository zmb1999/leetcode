def findContinuousSequence(target):
    i, j = 1, 1
    sum = 0
    res = []
    while i <= target // 2:
        if sum < target:
            sum += j
            j += 1
        elif sum > target:
            sum -= i
            i += 1
        else:
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            sum -= i
            i += 1
    return res

print(findContinuousSequence(15))