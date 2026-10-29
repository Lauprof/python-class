try:
    score = int(input("Enter the score (0-100): "))
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
    elif score >= 80:
        print("A Excellent")
    elif score >= 70:
        print("B Good")
    elif score >= 60:
        print("C Average")
    elif score >= 50:
        print("D Poor")
    else:
        print("E Fail")
except ValueError:
    print("Invalid input. Please enter a numeric value for the score.")


