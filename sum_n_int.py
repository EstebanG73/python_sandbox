# sum the first n integers
n = int(input("Enter a integer greater than 0: "))
total = 0
c = 1
while c <= n:
    total += c
    c += 1

print("The sum of the first ", n, " natural numbers is = ", total)

input("Press Enter to exit")

