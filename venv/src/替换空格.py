def replaceSpace(s):
    # write code here
    res = []
    for i in range(len(s)):
        if s[i] == " ":
            res.append("%20")
        else:
            res.append(s[i])
    return "".join(res)

print(replaceSpace("hello world"))