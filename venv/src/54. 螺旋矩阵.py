# def spiralOrder(matrix):
#     if not matrix: return []
#     m, n = len(matrix), len(matrix[0])
#     l, r, t, b = 0, n - 1, 0, m - 1
#     mat = []
#     num, tar = 1, m * n
#     while num <= tar:
#         for i in range(l, r + 1):
#             mat.append(matrix[t][i])
#             num += 1
#         t += 1
#         if num > tar: break
#         for i in range(t, b + 1):
#             mat.append(matrix[i][r])
#             num += 1
#         r -= 1
#         if num > tar: break
#         for i in range(r, l - 1, -1):
#             mat.append(matrix[b][i])
#             num += 1
#         b -= 1
#         if num > tar: break
#         for i in range(b, t - 1, -1):
#             mat.append(matrix[i][l])
#             num += 1
#         l += 1
#         if num > tar: break
#     return mat

# def spiralOrder(matrix):
#     if not matrix: return []
#     R, C = len(matrix), len(matrix[0])
#     seen = [[False] * C for _ in matrix]
#     ans = []
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     r = c = di = 0
#     for _ in range(R * C):
#         ans.append(matrix[r][c])
#         seen[r][c] = True
#         cr, cc = r + dr[di], c + dc[di]
#         if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
#             r, c = cr, cc
#         else:
#             di = (di + 1) % 4
#             r, c = r + dr[di], c + dc[di]
#     return ans

def spiralOrder(matrix):
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    if not matrix: return []
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            ans.append(matrix[r][c])
        r1 += 1;
        r2 -= 1
        c1 += 1;
        c2 -= 1
    return ans

print(spiralOrder([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
      )