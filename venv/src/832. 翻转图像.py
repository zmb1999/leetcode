def flipAndInvertImage(A):
    i = 0
    for row in A:
        row = row[::-1]
    for row in A:
        for j in range(len(row)):
            row[j] = 1 - row[j]
    return A

# def flipAndInvertImage( A) :
#     for row in A:
#         for k, _ in enumerate(row):
#             row[k] = 1 - row[k]  # Python 风格的循环, 1和0反转
#         i, j = 0, len(row) - 1
#         while i < j:
#             row[i], row[j] = row[j], row[i]  # Python 特有的交换
#             i, j = i + 1, j - 1
#     return A


print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
