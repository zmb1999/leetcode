from functools import lru_cache


class Solution:
    def isInterleave(self, s1, s2, s3):
        # 边界情况
        if len(s1) + len(s2) != len(s3): return False
        @lru_cache()
        def _dfs(i, j, k):
            # 递归结束条件
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i > len(s1) or j > len(s2) or k > len(s3):
                return False

            # s1 和 s3 的字符相匹配
            if i < len(s1) and k < len(s3) and s1[i] == s3[k] and _dfs(i + 1, j, k + 1):
                return True

            # s2 和 s3 的字符相匹配
            if j < len(s2) and k < len(s3) and s2[j] == s3[k] and _dfs(i, j + 1, k + 1):
                return True

            return False

        return _dfs(0, 0, 0)

import time
start = time.time()
s =Solution()
print(s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
end = time.time()

print("时间成本：",end - start)