# Part 1: Grade Calculator, Extended

def get_valid_score(score_name):
    """Prompts for a score and validates it is between 0 and 100."""
    while True:
        try:
            score = float(input(f"Enter {score_name} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

# Input validation loop for 3 scores
score1 = get_valid_score("Score 1")
score2 = get_valid_score("Score 2")
score3 = get_valid_score("Score 3")

# Calculate average
average = (score1 + score2 + score3) / 3
print(f"\nAverage Score: {average:.2f}")

# Determine letter grade using elif chain
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'F'

print(f"Letter Grade: {grade}")

# Tutor recommendation check
if average < 70:
    print("Recommendation: Please schedule a meeting with a tutor.")