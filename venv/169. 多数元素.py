#哈希表法
def majorityElement1(nums):
    dict = {}
    for num in nums:
        dict[num] = 0
    # print(dict)
    for num in nums:
        dict[num] += 1
    return max(dict.keys(), key=dict.get)
    # counts = collections.Counter(nums)
    # return max(counts.keys(), key=counts.get)

# 投票法
def majorityElement2( nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
