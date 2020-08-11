# def maxSubArray(nums):    #时间复杂度O(n^2)
#     dp = []
#     for i in range(len(nums)):
#         sums = -10000
#         tmp = 0
#         for j in range(i, len(nums)):
#             tmp += nums[j]
#             sums = max(tmp, sums)
#         dp.append(sums)
#     return max(dp)

def maxSubArray(nums):      #时间复杂度O(n)
    tmp = nums[0]
    res = tmp
    for i in range(1, len(nums)):
        if tmp > 0:
            tmp += nums[i]
            res = max(res, tmp)
        else:
            tmp = nums[i]
            res = max(res, tmp)
    return res

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))