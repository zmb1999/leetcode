def isPalindrome(n):
    if n < 0:
        return False
    x = n
    m = 0
    temp = 0
    while n:
        m = m * 10 + n % 10
        print(m)
        temp = m
        n = n // 10 #注意取整

    if x == m:
        return True
    else:
        return False

a = isPalindrome(121)
print(a)