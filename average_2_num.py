# Function to calculate the average of two numbers

def average2(x, y):
    p = (x + y)/2
    return p

print("Enter 2 numbers:\n")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(f"\nThe average of {a} and {b} is equal to {average2(a, b)}\n")

input("Press Enter to exit")

