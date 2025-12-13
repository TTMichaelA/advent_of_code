import re 

def render_line(string):
    return list(map(int,re.findall("[0-9]+", string)))

def valid(report):
    incr = True
    if report[0] > report[1]:
        incr = False
    
    for i in range(0, len(report) - 1):
        if abs(report[i] - report[i+1]) > 3:
            return False
        if incr:
            if report[i] > report[i+1]:
                return False
        else:
            if report[i] < report[i+1]:
                return False
        if report[i] == report[i+1]:
            return False
    return True 

def dampen(report):
    for i in range(len(report)):
        report_copy = report.copy()
        del report_copy[i]
        if valid(report_copy):
            return True
    return False


if __name__ == "__main__":
    n_valid = 0
    n_dampen = 0
    cnt = 0
    with open("day2_input.py") as input:
        for line in input:
            line = line.strip("\n")
            cnt += 1
            report = render_line(line)
            if valid(report):
                n_valid += 1
            if dampen(report):
                n_dampen +=1
    print(f"cnt is {cnt} and number valid is {n_valid}")
    print(f"dampen is {n_dampen}")