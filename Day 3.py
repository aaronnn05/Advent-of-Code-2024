import re

def add_mul(file_path):
    with open(file_path, "r") as file:
        complete_memory = re.sub(r"don't\(\).*?(do\(\)|$)", "", file.read(), flags=re.DOTALL)
                                                        #".*? doesn't match \n without re.DOTALL"
        return sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", complete_memory))
                                                        #Use r"" when using \ in regex to prevent conflicts with python's \
def main():
    print(f"Results of multiplications: {add_mul('Day 3 Input.txt')}")

if __name__ == "__main__":
    main()

# total1 = total2 = 0
# enabled = True
# data = open(...).read()

# for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
#     if do or dont:
#         enabled = bool(do)
#     else:
#         x = int(a) * int(b)
#         total1 += x
#         total2 += x * enabled

# print(total1, total2)


