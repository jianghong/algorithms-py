'''
Given a 2D array that represents a Sudoku board,
check if it's a valid solution.
'''


def sudoku_checker(board):
    def _check_numbers(A):
        for i in xrange(1, 10):
            if A[i-1] != i:
                return False
        return True

    def _check_rows(board):
        for row in board:
            row = sorted(row)
            if not _check_numbers(row):
                return False
        return True


    def _check_columns(board):
        for i in xrange(9):
            column = []
            for j in xrange(9):
                column.append(board[j][i])
            column = sorted(column)
            if not _check_numbers(column):
                return False

        return True

    def _check_grids(board):
        for i in xrange(3):
            r = i*3
            grid1 = []
            grid2 = []
            grid3 = []            
            for j in xrange(r, r+3):
                for k in xrange(3):
                    grid1.append(board[k][j])
                for k in xrange(3, 6):
                    grid2.append(board[k][j])
                for k in xrange(6, 9):
                    grid3.append(board[k][j])

            grid1 = sorted(grid1)
            grid2 = sorted(grid2)
            grid3 = sorted(grid3)

            if not (_check_numbers(grid1) and _check_numbers(grid2) and _check_numbers(grid3)):
                return False

        return True




    return _check_rows(board) and _check_columns(board) and _check_grids(board)

if __name__ == '__main__':
    b1 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]

    b2 = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    assert sudoku_checker(b1) == False
    assert sudoku_checker(b2) == True
