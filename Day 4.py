def load_puzzle(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]
    
def parse_puzzle(puzzle, variants, idx_lsts, total = 0):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            for idx_lst in idx_lsts:
                try:
                    if "".join(puzzle[y + dy][x + dx] for dx, dy in idx_lst) in variants:
                        total += 1
                except IndexError:
                    pass
                
    return total

def main():
    variants1 = {"XMAS", "SAMX"}
    variants2 = {"MASMS", "SAMMS", "MASSM", "SAMSM"}
    idx_lsts1 = [[(0, 0), (0, 1), (0, 2), (0, 3)], #Vertical
               [(0, 0), (1, 0), (2, 0), (3, 0)],  #Horizontal
               [(0, 0), (1, 1), (2, 2), (3, 3)],  #Diagonal
               [(0, 3), (1, 2), (2, 1), (3, 0)]]  #Other Diagonal
    idx_lsts2 = [[(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]]
    #Cannot use negative indices cuz python will take it literally instead of going out of bounds
    
    puzzle = load_puzzle("Day 4 Input.txt")
    print(f"Total times that XMAS appear: {parse_puzzle(puzzle, variants1, idx_lsts1)}")
    print(f"Total times that X-MAS appear: {parse_puzzle(puzzle, variants2, idx_lsts2)}")

if __name__ == "__main__":
    main()