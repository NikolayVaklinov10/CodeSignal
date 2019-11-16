"""
Sudoku

"""


def sudoku2(grid):
    def dup_in_list(lst):
        numbers_only = [n for n in lst if n != '.']
        print(numbers_only)
        return len(numbers_only) > len(set(numbers_only))

    dups_in_rows = any(dup_in_list(row) for row in grid)
    dups_in_cols = any(dup_in_list([grid[r][c] for r in range(0, 9)]) for c in range(9))
    subgrids = [[] for i in range(9)]
    for r in range(9):
        for c in range(9):
            subgrids[3 * (r // 3) + c // 3].append(grid[r][c])
    dups_in_subgrids = any(dup_in_list(s) for s in subgrids)

    return not (dups_in_rows or dups_in_cols or dups_in_subgrids)
