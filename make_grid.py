import random

class Sudoku:
    def __init__(self, K):
        self.grid = [[0]*9 for _ in range(9)]
        self.K = K

    def fillValues(self):
        self.fillDiagonal()
        self.fillRemaining(0, 3)
        self.removeKDigits()

    def fillDiagonal(self):
        for i in range(0, 9, 3):
            self.fillBox(i, i)

    def unUsedInBox(self, rowStart, colStart, num):
        for i in range(3):
            for j in range(3):
                if self.grid[rowStart + i][colStart + j] == num:
                    return False
        return True

    def fillBox(self, row, col):
        for i in range(3):
            for j in range(3):
                while True:
                    num = self.randomGenerator(9)
                    if self.unUsedInBox(row, col, num):
                        break
                self.grid[row + i][col + j] = num

    def randomGenerator(self, num):
        return random.randint(1, num+1)

    def CheckIfSafe(self, i, j, num):
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and
                self.unUsedInBox(i - i % 3, j - j % 3, num))

    def unUsedInRow(self, i, num):
        return not num in self.grid[i]

    def unUsedInCol(self, j, num):
        return not num in [self.grid[i][j] for i in range(9)]

    def fillRemaining(self, i, j):
        if i == 8 and j == 9:
            return True
        if j == 9:
            i += 1
            j = 0
        if self.grid[i][j] != 0:
            return self.fillRemaining(i, j + 1)
        for num in range(1, 10):
            if self.CheckIfSafe(i, j, num):
                self.grid[i][j] = num
                if self.fillRemaining(i, j + 1):
                    return True
        self.grid[i][j] = 0
        return False

    def removeKDigits(self):
        count = self.K
        while count != 0:
            cellId = self.randomGenerator(81) - 1
            i = int(cellId / 9)
            j = cellId % 9
            if j != 0:
                j -= 1
            if self.grid[i][j] != 0:
                count -= 1
                self.grid[i][j] = 0

    def printSudoku(self):
        for i in range(9):
            for j in range(9):
                print(str(self.grid[i][j]) + " ", end='')
            print()

if __name__ == "__main__":
    K = 60
    random.seed()
    sudoku = Sudoku(K)
    sudoku.fillValues()
    sudoku.printSudoku()
