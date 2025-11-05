def solve_n_queens(n, find_one=False):
    solutions = []
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [-1] * n

    def place(row):
        if row == n:
            sol = []
            for r in range(n):
                row_str = ['.'] * n
                row_str[board[r]] = 'Q'
                sol.append(''.join(row_str))
            solutions.append(sol)
            return find_one  # True means stop early (bubble up)
        for c in range(n):
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue
            cols.add(c); diag1.add(row - c); diag2.add(row + c); board[row] = c
            stop = place(row + 1)
            cols.remove(c); diag1.remove(row - c); diag2.remove(row + c); board[row] = -1
            if stop:
                return True
        return False

    place(0)
    return solutions

if __name__ == "__main__":
    N = 8
    sols = solve_n_queens(N)         # all solutions
    print("Total:", len(sols))
    if sols:
        print("One solution:")
        print('\n'.join(sols[0]))
