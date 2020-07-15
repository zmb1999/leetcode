def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    import numpy as np
    r, c = len(board), len(board[0])
    # 下面两行做zero padding
    board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
    board_exp[1:1 + r, 1:1 + c] = np.array(board)
    # 设置卷积核
    print(board_exp)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    # 开始卷积
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            # 统计细胞周围8个位置的状态
            temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
            # 按照题目规则进行判断
            if board_exp[i, j] == 1:
                if temp_sum < 2 or temp_sum > 3:
                    board[i - 1][j - 1] = 0
            else:
                if temp_sum == 3:
                    board[i - 1][j - 1] = 1
    return board

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))