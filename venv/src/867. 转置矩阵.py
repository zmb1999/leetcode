def transpose( A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    B = [[0] * len(A) for i in range(len(A[0]))]    #开辟一个len(A)*len(A[0])的矩阵
    #print(B,len(A))
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = A[j][i]
    return B

print(transpose([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))