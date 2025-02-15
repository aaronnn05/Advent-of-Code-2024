import re

def add_mul(file_path):
    with open(file_path, "r") as file:
        return sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file.read()))
                                                        #Use r"" when using \ in regex to prevent conflicts with python's \
def main():
    print(f"Results of multiplications: {add_mul("Day 3 Input.txt")}")

if __name__ == "__main__":
    main()