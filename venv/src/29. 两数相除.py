# def divide( dividend, divisor):       #超时
#     num = 0
#     cnt = 0
#     if dividend < 0:
#         temp_dividend = -dividend
#     else:
#         temp_dividend = dividend
#     if divisor < 0:
#         temp_divisor = -divisor
#     else:
#         temp_divisor = divisor
#     while cnt <= temp_dividend:
#         cnt += temp_divisor
#         # print(cnt)
#         if cnt <= temp_dividend:
#             num += 1
#     if (dividend < 0) ^ (divisor < 0):
#         num = -num
#     return num
def divide(dividend, divisor):      #通过位运算每次逼近2^n
    sign = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    #把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
            dividend -= divisor
    if sign: result = -result
    return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1

print(divide(-2147483648,-1))