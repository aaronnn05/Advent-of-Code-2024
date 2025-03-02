def load_rules(file_path):
    with open(file_path, "r") as file:
        return {tuple(line.strip().split("|")) for line in file}
    
def load_pages(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split(",") for line in file]
    
def abide_rules(rules, update):
    return (
        len(update) == 1
        or not any((update[i], update[0]) in rules for i in range(len(update)))
        and abide_rules(rules, update[1:])
    )

def parse_updates(rules, updates):
    total = 0
    for update in updates:
        if abide_rules(rules, update):
            continue
        else:
            while not abide_rules(rules, update):
                for i in range(len(update)):
                    for j in range(i, len(update)):
                        if (update[j], update[i]) in rules:
                            update[i], update[j] = update[j], update[i]     #Bubble sort
            total += int(update[len(update)//2])
    return total

def main():
    ordering_rules = load_rules("Day 5 Input 1.txt")
    pages_updates = load_pages("Day 5 Input 2.txt")
    total = parse_updates(ordering_rules, pages_updates)
    print(f"Total middle page number: {total}")

if __name__ == "__main__":
    main()