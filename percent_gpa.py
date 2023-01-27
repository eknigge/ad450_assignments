import sys

def calculate_gpa(score: float) -> float:
    score = float(score)
    if score >= 95:
        return 4.0
    elif score < 65:
        return 0.0
    
    gpa = 3.9 # start GPA value
    upper_score = 95 # start percentage value
    while upper_score > 65:
        lower_score = upper_score - 1
        if score < 95 and score >= lower_score:
            return round(gpa, 1)
        gpa -= .1
        upper_score -= 1

if __name__ == '__main__':
    print(calculate_gpa(sys.argv[1]))