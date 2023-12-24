# Sprawdzam czy jest symbol
def checkSymbol(char):
    return char != '.' and not char.isdigit()

# Sprawdzanie sąsiadów
def checkNeighbors(grid, x, y):
    # Kierunki do sprawdzania
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    # Długości i wysokość grid
    rows = len(grid)
    cols = len(grid[0])

    for dx, dy in directions:
        if 0 <= (x+dx) < rows and 0 <= (y+dy) < cols and checkSymbol(grid[(x+dx)][(y+dy)]):
            return True

    return False