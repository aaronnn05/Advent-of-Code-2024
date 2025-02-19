def load_puzzle(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]
    
def generate_directions(puzzle):
    total_x = len(puzzle[0])
    total_y = len(puzzle)
    xy_directions = [(dx, dy) for dx, dy in range(-1, 2) if not (dx == 0 and dy == 0)]

    return total_x, total_y, xy_directions
