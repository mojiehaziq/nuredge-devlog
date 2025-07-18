# Mini Project 5.1: Number Categorizer

numbers = []

# Collect 5 numbers from user
for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print("\nResults:")

# Analyze each number
for num in numbers:
    result = ""
    # Check even/odd
    if num % 2 == 0:
        result += "Even"
    else:
        result += "Odd"

    # Check greater than 10
    if num > 10:
        result += " and Greater than 10"
    else:
        result += " and Not greater than 10"

    print(f"{num} is {result}")
