count = 0


def display(n, board):
    global count
    count += 1
    # for i in range(n):
    #     for j in range(n):
    #         print(board[i][j], end=" ")
    #     print()

    # print()


def check(row, col, board):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i = row-1
    j = col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row-1
    j = col+1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def NQueens(row, n, board):
    if row == n:
        display(n, board)
        return True

    for col in range(n):
        if check(row, col, board):
            board[row][col] = 'Q'
            NQueens(row+1, n, board)
            board[row][col] = '.'
    return False


n = int(input())
board = [['.' for i in range(n)] for i in range(n)]
NQueens(0, n, board)
print(count)
