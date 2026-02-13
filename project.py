
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]



def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))



def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_valid(grid, num, row, col):

 
    if num in grid[row]:
        return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    box_row = row // 3 * 3
    box_col = col // 3 * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False

    return True



def solve(grid):

    empty = find_empty(grid)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, row, col):

            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False


print("Original Sudoku:\n")
print_grid(sudoku)

if solve(sudoku):
    print("\nSolved Sudoku:\n")
    print_grid(sudoku)
else:
    print("No solution exists")
