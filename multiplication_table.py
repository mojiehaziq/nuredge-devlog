# Mini Project 3: Multiplication Table Generator

def print_table(number):
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Get user input
num = int(input("Enter a number to see its multiplication table: "))

# Call function
print_table(num)
