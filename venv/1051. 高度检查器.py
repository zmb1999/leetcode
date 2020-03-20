# def heightChecker(self, heights: List[int]) -> int:     #排序比较做法，时间复杂度O(Nlog(N))
#     sort_heights = sorted(heights)
#     count = 0
#     for i in range(len(heights)):
#         if sort_heights[i] != heights[i]:
#             count += 1
#     return count

#去他妈的哈希表

print(heightChecker([1,2,1,2,1,1,1,2,1]))