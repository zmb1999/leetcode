# def sortedSquares(self, A: List[int]) -> List[int]:     #排序做法，一行
#     return sorted(x * x for x in A)

def sortedSquares(self, A: List[int]) -> List[int]:         #双指针做法
    N = len(A)
    # i, j: negative, positive parts
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
        if A[i]**2 < A[j]**2:
            ans.append(A[i]**2)
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1

    while i >= 0:
        ans.append(A[i]**2)
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans

# def sortedSquares(self, A: List[int]) -> List[int]:       #排序做法
#     for i in range(len(A)):
#         A[i] = abs(A[i])
#     A.sort()
#     for i in range(len(A)):
#         A[i] = A[i] ** 2
#     return A