def romanToInt(self, s: str) -> int:
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(s)):
        if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:  # 注意数组越界
            num -= a[s[i]]
        else:
            num += a[s[i]]
    return num