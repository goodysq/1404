def main():
    """get score and level it"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(f"{score} is {level_of_score(score)}!")


def level_of_score(score):
    """give level base on the score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
