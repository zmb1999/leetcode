def lengthOfLongestSubstring(s):
    lookup = set()#滑动窗口
    left = 0
    max_len = 0
    length = 0
    for i in range(len(s)):
        length += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            length -=1
        if length > max_len:
            max_len = length
        lookup.add(s[i])
    return max_len

def LongestSubstring(s):    #更快更强
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
            print(i)
            print(st[s[j]])
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
        print(st)
    return ans;

print(LongestSubstring("adbbcabcbb"))