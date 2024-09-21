# Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through the numbers 1 to 10.
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")