def findWords(words):
    set1 = set('qwertyuiop')
    set2 = set('asdfghjkl')
    set3 = set('zxcvbnm')
    res = []
    for i in words:
        x = i.lower()
        setx = set(x)
        if setx <= set1 or setx <= set2 or setx <= set3:    #s <= t     测试是否 s 中的每一个元素都在 t 中
            res.append(i)

    return res

print(findWords(["Hello","Alaska","Dad","Peace"]))