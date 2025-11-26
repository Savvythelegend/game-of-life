import random 
ROW,COL = 10, 10


def create_grid():
    grid = [[random.choice([0,1]) for _ in range (COL)] for _ in range(ROW)]    
    return grid


def count_neighbors(grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROW and 0 <= nc < COL:
                count += grid[nr][nc]
    return count

def update(grid):
    new_grid = [[0] * COL for _ in range(ROW)]
    for rc in range (ROW):
        for cc in range (COL):
            n = count_neighbors(grid, rc, cc)
            if grid[rc][cc] == 1 and n in [2,3]:
                new_grid[rc][cc] = 1
            elif grid[rc][cc] == 0 and n == 3:
                new_grid[rc][cc] = 1 
    return new_grid


def show_grid(grid):
    for row in grid:
        print(" ".join('#' if x else '.' for x in row))
    print()



while True:
    inp = input("Press Enter to continue, 'q' to quit: ")
    if inp.lower() == 'q':
        break
    grid = create_grid()
    show_grid(grid)
    for _ in range(50): # for 5 generations
        grid = update(grid)
        show_grid(grid)