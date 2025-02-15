import re

def add_mul(file_path):
    total = 0
    with open(file_path, "r") as file:
        for line in file:
            results = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
            results = [list(map(int, result)) for result in results]
            total += sum(lst[0]*lst[1] for lst in results)

    return total

def main():
    print(f"Results of multiplications: {add_mul("Day 3 Input.txt")}")

if __name__ == "__main__":
    main()