def load_puzzle(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]
    
def parse_puzzle(table, total = 0):
    variants = ["XMAS", "SAMX"]
    idx_lsts = [[(0, 0), (0, 1), (0, 2), (0, 3)], #Vertical
               [(0, 0), (1, 0), (2, 0), (3, 0)],  #Horizontal
               [(0, 0), (1, 1), (2, 2), (3, 3)],  #Top Right
               [(0, 0), (1, -1), (2, -2), (3, -3)]] #Bottom Right

    for row_idx in range(len(table)):
        for col_idx in range(len(table[0])):
            for idx_lst in idx_lsts:
                try:
                    if "".join(table[row_idx + dy][col_idx + dx] for dy, dx in idx_lst) in variants:
                        total += 1
                except IndexError:
                    pass
                
    return total

def main():
    puzzle = load_puzzle("Day 4 Input.txt")
    print(f"Total times that XMAS appear: {parse_puzzle(puzzle)}")

if __name__ == "__main__":
    main()