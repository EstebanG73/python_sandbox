# Product of two numbers using a function

def product2(x, y):
    p = x * y
    return p

print("Enter 2 numbers\n")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(f"\nThe product of {a} and {b} is equal to {product2(a, b)}\n")

input("Press Enter to exit")
