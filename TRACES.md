# TRACES.md

## 1. Grade Calculator Trace (Boundary Case = 70)

* **Inputs:** 70, 70, 70

| Step | Line | Variable / Action | Value / Output |
| :--- | :--- | :--- | :--- |
| 1 | 11 | `score1` | 70.0 |
| 2 | 12 | `score2` | 70.0 |
| 3 | 13 | `score3` | 70.0 |
| 4 | 16 | `average` | 70.0 |
| 5 | 17 | Output | "Average Score: 70.00" |
| 6 | 20 | `average >= 90` | False |
| 7 | 22 | `average >= 80` | False |
| 8 | 24 | `average >= 70` | True -> `grade = 'C'` |
| 9 | 29 | Output | "Letter Grade: C" |
| 10 | 32 | `average < 70` | False |


## 2. Guessing Game Trace (6 Attempts - Loss)

* **Secret Number:** 42
* **Input Sequence:** 10, 20, 30, 50, 60, 70

| Step | Line | `secret_number` | `max_guesses` | `guesses_used` | `guess` | `remaining` | Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 5 | 42 | 6 | 0 | - | - | (None) |
| 2 | 12 | 42 | 6 | 0 -> 1 | 10 | - | (None) |
| 3 | 17 | 42 | 6 | 1 | 10 | - | "Too low!" |
| 4 | 22 | 42 | 6 | 1 | 10 | 5 | "Guesses remaining: 5" |
| 5 | 12 | 42 | 6 | 1 -> 2 | 20 | 5 | (None) |
| 6 | 17 | 42 | 6 | 2 | 20 | 5 | "Too low!" |
| 7 | 22 | 42 | 6 | 2 | 20 | 4 | "Guesses remaining: 4" |
| 8 | 12 | 42 | 6 | 2 -> 3 | 30 | 4 | (None) |
| 9 | 17 | 42 | 6 | 3 | 30 | 4 | "Too low!" |
| 10 | 22 | 42 | 6 | 3 | 30 | 3 | "Guesses remaining: 3" |
| 11 | 12 | 42 | 6 | 3 -> 4 | 50 | 3 | (None) |
| 12 | 19 | 42 | 6 | 4 | 50 | 3 | "Too high!" |
| 13 | 22 | 42 | 6 | 4 | 50 | 2 | "Guesses remaining: 2" |
| 14 | 12 | 42 | 6 | 4 -> 5 | 60 | 2 | (None) |
| 15 | 19 | 42 | 6 | 5 | 60 | 2 | "Too high!" |
| 16 | 22 | 42 | 6 | 5 | 60 | 1 | "Guesses remaining: 1" |
| 17 | 12 | 42 | 6 | 5 -> 6 | 70 | 1 | (None) |
| 18 | 19 | 42 | 6 | 6 | 70 | 1 | "Too high!" |
| 19 | 22 | 42 | 6 | 6 | 70 | 0 | (None) |
| 20 | 25 | 42 | 6 | 6 | 70 | 0 | "Out of guesses!" / "The secret number was: 42" |

## 3. Custom FizzBuzz Trace (Number 105)

* **Input (`i`):** 105

| Step | Line | `i` | `output` | Condition Evaluated | Result / Action | Output Stream |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 3 | 105 | `""` | Loop Start | Initialize `output` | (None) |
| 2 | 6 | 105 | `""` | `105 % 3 == 0` | True -> `output += "Fizz"` | (None) |
| 3 | 8 | 105 | `"Fizz"` | `105 % 5 == 0` | True -> `output += "Buzz"` | (None) |
| 4 | 10 | 105 | `"FizzBuzz"` | `105 % 7 == 0` | True -> `output += "Bang"` | (None) |
| 5 | 13 | 105 | `"FizzBuzzBang"` | `item = output if output else str(i)` | Sets `item = "FizzBuzzBang"` | (None) |
| 6 | 16 | 105 | `"FizzBuzzBang"` | `105 % 10 == 0` | False -> Executes `else` block | "FizzBuzzBang " |