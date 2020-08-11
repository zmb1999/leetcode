# def countBits(num):       #时间复杂度O(n*K),K是x的位数
#     res = []
#     for i in range(num + 1):
#         count = 0
#         while i != 0:
#             i &= i - 1
#             count += 1
#         res.append(count)
#     return res

def countBits(num):     #动态规划，时间复杂度为O(n)
    res = [0]
    for i in range(1,num+1):
        #print(i)
        if i % 2 == 1:
            res.append(res[i-1] + 1)
        else:
            res.append(res[i//2])
    return res