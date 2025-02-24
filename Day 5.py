def load_rules(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split("|") for line in file]
    
