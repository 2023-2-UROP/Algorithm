grid = [[0] * 9 for _ in range(9)]


def printGrid():
    print("\n┌──────────┬───────────┬──────────┐")
    for row in range(9):
        print("│", end='')
        for col in range(9):
            print(f" {grid[row][col]} ", end='')
            if col == 2 or col == 5:
                print("│", end=' ')
        print("│")
        if row == 2 or row == 5:
            print("├──────────┼───────────┼──────────┤")
    print("└──────────┴───────────┴──────────┘\n")


def isPossible():
    filled_cell = 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                filled_cell += 1
    return filled_cell >= 17


def isRow(row, num):
    return num in grid[row]


def isCol(col, num):
    return num in [grid[i][col] for i in range(9)]


def isSubGrid(start_row, start_col, num):
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return True
    return False


def isValid(row, col, num):
    start_row = row - row % 3
    start_col = col - col % 3
    return not isRow(row, num) and not isCol(col, num) and not isSubGrid(start_row, start_col, num)


def findEmptyCell():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def solve_sudoku():
    row, col = findEmptyCell()
    if row is None:
        return True

    for num in range(1, 10):
        if isValid(row, col, num):
            grid[row][col] = num
            if solve_sudoku():
                return True
            grid[row][col] = 0
    return False


if __name__ == "__main__":
    filled = 0
    for i in range(9):
        grid[i] = list(map(int, input().split()))
        filled += sum(1 for x in grid[i] if x > 0)

    print(f"채워진 셀의 수: {filled}")

    if not isPossible():
        print("불가능한 스도쿠 퍼즐입니다.")
    else:
        if solve_sudoku():
            print("성공!")
            printGrid()
        else:
            print("실패!")
