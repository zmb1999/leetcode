class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:      #位掩码的思想
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res
