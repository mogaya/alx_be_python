# Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
pattern_size = int(input("Enter the size of the pattern: "))

count = 0
while count < pattern_size:
    for i in range(1, pattern_size+1):
        print("*", end = "")
    count += 1
    print()