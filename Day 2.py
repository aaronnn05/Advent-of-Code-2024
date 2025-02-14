def load_reports(file_path):
    with open(file_path, "r") as file:
        reports = [list(map(int, line.strip().split())) for line in file]

    return reports

def check_rules_recursive(report, increasing = True, decreasing = True):
    if len(report) == 1:
        return True
    diff = report[1] - report[0]
    if (diff > 0 and increasing or diff < 0 and decreasing) and 1 <= abs(diff) <= 3:
        return check_rules_recursive(report[1:], diff > 0, diff < 0)
    return False
    
def analyse_report(report):
    if check_rules_recursive(report):
        return True
    return any(check_rules_recursive(report[:i] + report[i+1:]) for i in range(len(report)))

def analyse_data(reports):
    return sum(map(analyse_report, reports))
    #return sum(any(check_rules_recursive(report[:i] + report[i+1:]) for i in range(len(report))) for report in reports)

def main():
    reports = load_reports("Day 2 Input.txt")
    print(f"Number of safe reports: {analyse_data(reports)}")

if __name__ == "__main__":
    main()