# Sum 4 numbers using input() and functions

def sum4(a, b, c, d):
    r =  a + b + c + d
    return r

print("Sum 4 numbers:\n\n")
x = float(input("Enter the first number = "))
y = float(input("Enter the second number = "))
z = float(input("Enter the third number = "))
w = float(input("Enter the fourth number = "))
print("The result is : ", sum4(x, y, z, w))
input("Press Enter to exit")
