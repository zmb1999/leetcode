class Solution:
    def __init__(self):
        self.lists = []

    def judge(self, num):
        temp = num
        while temp != 0:
            if num % (temp % 10) != 0 or temp % 10 == 0:
                return False
            temp = temp // 10
        return True

    def selfDividingNumbers(self, left, right):
        self.lists = []
        for num in range(left, right + 1):
            if self.judge(num):
                lists.append(num)
        return lists

solution = Solution()
solution.selfDividingNumbers(1,10)