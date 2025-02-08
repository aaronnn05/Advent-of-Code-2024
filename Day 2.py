def load_reports(file_path):
    with open(file_path, "r") as file:
        reports = [list(map(int, line.strip().split())) for line in file]

    return reports

def check_rules_recursive(report):
    increasing, decreasing = True, True
    if len(report) == 1:
        return True
    elif (report[0] < report[1]) and 1 <= (report[1] - report[0]) <= 3 and increasing:
        decreasing = False
        return check_rules_recursive(report[1:])
    elif (report[0] > report[1]) and 1 <= (report[0] - report[1]) <= 3 and decreasing:
        increasing = False
        return check_rules_recursive(report[1:])
    else:
        return False
    
def analyse_data(reports):
    return sum(1 if map(check_rules_recursive, report) else 0 for report in reports)

def main():
    reports = load_reports("Day 2 Input.txt")
    print(f"Number of safe reports: {analyse_data(reports)}")

if __name__ == "__main__":
    main()