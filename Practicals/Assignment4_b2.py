N = 8


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(row, col, slashcode, backslashcode, rowlookup, slashCodeLookup, backslashCodeLookup):

    if(slashCodeLookup[slashcode[row][col]] or backslashCodeLookup[backslashcode[row][col]] or rowlookup[row]):
        return False
    return True


def NQeens(board, col, slashcode, backslashcode, rowlookup, slashCodeLookup, backslashCodeLookup):

    if col >= N:
        return True
    for i in range(N):
        if(isSafe(i, col, slashcode, backslashcode, rowlookup, slashCodeLookup, backslashCodeLookup)):
            board[i][col] = 1
            rowlookup[i] = True
            slashCodeLookup[slashcode[i][col]] = True
            backslashCodeLookup[backslashcode[i][col]] = True

            if(NQeens(board, col+1, slashcode, backslashcode, rowlookup, slashCodeLookup, backslashCodeLookup)):
                return True

            board[i][col] = 0
            rowlookup[i] = False
            slashCodeLookup[slashcode[i][col]] = False
            backslashCodeLookup[backslashcode[i][col]] = False
    return False


def solve():
    board = [[0 for i in range(N)] for j in range(N)]

    slashcode = [[0 for i in range(N)] for j in range(N)]

    backslashcode = [[0 for i in range(N)] for j in range(N)]

    rowlookup = [False]*N
    x = 2*N - 1
    slashCodeLookup = [False] * x
    backslashCodeLookup = [False] * x

    for row in range(N):
        for col in range(N):
            slashcode[row][col] = row+col
            backslashcode[row][col] = row-col + 7

    if(NQeens(board, 0, slashcode, backslashcode, rowlookup, slashCodeLookup, backslashCodeLookup) == False):
        print("Solution Does not Exists")
        return

    printSolution(board)
    return


solve()
