# Part 3: Custom FizzBuzz

for i in range(1, 51):
    output = ""
    
    # Check multiples and build string
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 7 == 0:
        output += "Bang"
    
    # Print combined word if any matched, otherwise print the number
    if output:
        print(output)
    else:
        print(i)