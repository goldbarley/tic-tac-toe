GRID_SIZE = 5

GRID = [[" "] * GRID_SIZE for i in range(GRID_SIZE)]

def initialize_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if j % 2 != 0 and i % 2 == 0:
                GRID[i][j] = "|"
            elif j % 2 != 0 and i % 2 != 0:
                GRID[i][j] = "+"
            elif j % 2 == 0 and i % 2 != 0:
                GRID[i][j] = "-"


def print_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(GRID[i][j], end=" ")
        print()
    print()

initialize_grid()