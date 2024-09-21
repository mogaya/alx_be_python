# Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Implement a Match Case statement that executes the chosen operation based on the user’s input.
match operation:
    case "+":
        result = num1+num2
        print("The result is ", result)
    case "-":
        result = num1-num2
        print("The result is ", result)
    case "*":
        result = num1 * num2
        print("The result is ", result)
    case "/" :
        if num2 == 0:
            print("Cannot divide by zero.")
        else:   
            result = num1/num2
            print("The result is ", result)