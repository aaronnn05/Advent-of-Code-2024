def load_puzzle(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]
    
def generate_directions(puzzle):
    # dd = [(-1, -1), (-1, 0), (-1, 1),
    #       (0, -1),           (0, 1),
    #       (1, -1), (1, 0), (1, 1)]

    return [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not (dx == 0 and dy == 0)]

def parse_puzzle(puzzle, x, y, direction):
    dx, dy = direction
    for offset, char in enumerate("XMAS"):
        sub_y = y + offset * dy
        sub_x = x + offset * dx
        if not(0 <= sub_y < len(puzzle) and 0 <= sub_x < len(puzzle[0])): # Check boundaries, no negative indices allowed
            return False
        if puzzle[sub_y][sub_x] != char:
            return False
    return True

# return all(
#     0 <= (sub_y := y + i * dy) < len(puzzle) and  
#     0 <= (sub_x := x + i * dx) < len(puzzle[0]) and  
#     puzzle[sub_y][sub_x] == "XMAS"[i]  
#     for i in range(4))

                    
def main():
    puzzle = load_puzzle("Day 4 Input.txt")
    xy_directions = generate_directions(puzzle)
    ans1 = sum(parse_puzzle(puzzle, x, y, d) for y in range(len(puzzle)) 
              for x in range(len(puzzle[0])) for d in xy_directions)
    print(f"Total XMAS: {ans1}")

if __name__ == "__main__":
    main()