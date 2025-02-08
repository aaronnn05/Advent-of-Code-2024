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