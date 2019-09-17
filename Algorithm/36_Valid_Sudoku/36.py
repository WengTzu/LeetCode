class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #print(board)
        for i in range(len(board)):
            #print(i)
            rows, cols, cube = set(), set(), set()
            for j in range(len(board[0])):
                print(i, j, '->', board[i][j])
                if board[i][j] != '.':
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])
                print(rows)
                if board[j][i] != '.':
                    if board[j][i] in cols:
                        return False
                    else:
                        cols.add(board[j][i])
                """
                0 1 2 3 4 5 6 7 8
                0 0 0 1 1 1 2 2 2 rowIndex
                0 1 2 0 1 2 0 1 2 i % 3
                0 3 6 0 3 6 0 3 6 colIndex

                0 0 0 1 1 1 2 2 2 j / 3
                0 1 2 0 1 2 0 1 2 j % 3

                i = 0, j = 0~8:
                0,0 + j[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] => Cube 0
                0,3
                0,6
                1,0
                1,3
                1,6
                2,0
                2,3
                2,6
                """
                rowIndex = 3 * int(i / 3)
                colIndex = 3 * (i % 3)
                print("rowIndex, colIndex", rowIndex, colIndex)
                print(int(rowIndex + j / 3), int(colIndex + j % 3))
                tmp = board[int(rowIndex + j / 3)][int(colIndex + j % 3)]
                if tmp != '.':
                    if tmp in cube:
                        return False
                    else:
                        cube.add(tmp)

if __name__ == '__main__':
    a = Solution()
    input = [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                ["",".",".",".","8",".",".","7","9"]
            ]
    sol = a.isValidSudoku(input)
    print("solution")        
    print(sol)