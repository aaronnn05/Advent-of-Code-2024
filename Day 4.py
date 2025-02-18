def load_puzzle(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]
    
def parse_puzzle(table, total = 0):
    for row_idx in range(len(table)):
        total += sum(search_everywhere(table, row_idx, col_idx) for col_idx in range(len(table[row_idx])) if table[row_idx][col_idx] == "X")
    return total