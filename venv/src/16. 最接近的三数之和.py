# def threeSumClosest(nums, target):
#     nums.sort()
#     if nums[len(nums) - 1] <= target:
#         return sum(nums[len(nums) - 3:len(nums)])
#     for i in range(len(nums)):
#         if nums[i] == target or (nums[i] < target and nums[i + 1] > target):
#             if i + 2 == len(nums):
#                 if abs(nums[i-2] + nums[i-1] + nums[i] - target) < abs(nums[i-1] + nums[i] + nums[i+1] - target):
#                     return nums[i-2] + nums[i-1] + nums[i]
#                 else:
#                     return nums[i-1] + nums[i] + nums[i+1]
#             else:
#                     if abs(nums[i-2] + nums[i-1] + nums[i] - target) < abs(nums[i-1] + nums[i] + nums[i+1] - target) and abs(nums[i-1] + nums[i] + nums[i+1] - target) < abs(nums[i] + nums[i+1] + nums[i+2] - target):
#                         return nums[i-1] + nums[i] + nums[i+1]
#                     elif abs(nums[i-1] + nums[i] + nums[i+1] - target) < abs(nums[i-1] + nums[i] + nums[i+1] - target) and abs(nums[i-1] + nums[i] + nums[i+1] - target) < abs(nums[i] + nums[i+1] + nums[i+2] - target):
#                         return
#             return

def threeSumClosest(nums, target):
    nums.sort()
    res = float('inf')
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return target
            elif s < target:
                j += 1
            else:
                k -= 1
            if abs(s - target) < abs(res - target):
                res = s
    return res

print(threeSumClosest([-1,2,1,-4],1))

# nums = [0,1,2,3,4,5,6,7,8,9]
# print(nums[len(nums) - 3:len(nums)])