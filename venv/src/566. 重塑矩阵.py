def matrixReshape1(nums, r, c):
    if len(nums) * len(nums[0]) != r * c:
        return nums
    ans = [[0] * c for _ in range(r)]
    i, j = 0, 0
    for line in nums:
        for num in line:
            ans[i][j] = num
            j = j + 1
            if j == c:
                j = 0
                i = i + 1
    return ans

def matrixReshape2(nums, r, c):
    if len(nums) * len(nums[0]) != r * c:
        return nums
    res = [[0] * c for _ in range(r)]
    # print(res)
    tmp = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            tmp.append(nums[i][j])
    for m in range(r):
        for n in range(c):
            res[m][n] = tmp[m * c + n]
    return res

def matrixReshape3(nums, r, c):
    if len(nums) * len(nums[0]) != r * c:
        return nums
    l = []
    new = []
    for i in range(len(nums)):
        l += nums[i]
    for i in range(0, len(l), c):
        new.append(l[i:i + c])
    return new