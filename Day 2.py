def load_reports(file_path):
    with open(file_path, "r") as file:
        reports = [list(map(int, line.strip().split())) for line in file]

    return reports

def check_rules_recursive(report, report_copy, idx = 0, increasing = True, decreasing = True, damp = False):
    if len(report) == 1:
        return True
    diff = report[1] - report[0]
    if damp and (diff > 0 and increasing or diff < 0 and decreasing) and 1 <= abs(diff) <= 3: 
        return check_rules_recursive(report[1:], report_copy, 0, diff > 0, diff < 0, True)
    elif (diff > 0 and increasing or diff < 0 and decreasing) and 1 <= abs(diff) <= 3:
        idx += 1
        return check_rules_recursive(report[1:], report_copy, idx, diff > 0, diff < 0)
    elif not damp:
        report_copy_1 = report_copy[:idx] + report_copy[idx+1:]
        report_copy_2 = report_copy[:idx+1] + report_copy[idx+2:]
        return check_rules_recursive(report_copy_1, report_copy_1, damp = True) or check_rules_recursive(report_copy_2, report_copy_2, damp = True) 
    return False
    
def analyse_data(reports):
    return sum(map(lambda report: check_rules_recursive(report, report), reports))

def main():
    reports = load_reports("Day 2 Input.txt")
    print(f"Number of safe reports: {analyse_data(reports)}")

if __name__ == "__main__":
    main()