# Compare two numbers and display the largest (using IF and functions)

def comp2(a, b):
    if a == b:
        print("\nThe two numbers are equal")
    elif a > b:
        print(f"\n{a} is greater than {b}")
    else:
        print(f"\n{b} is greater than {a}")
        
        
print("\nPlease enter 2 numbers:\n")

x = float(input("Enter the first number = "))
y = float(input("\nEnter the second number = "))

comp2(x, y)

input("\nPress Enter to exit")