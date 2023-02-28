# sum the first n even integers
n = int(input("Enter the number of even numbers: \n"))
total = 0
c = 0
while c <= n*2:
    total += c
    c += 2

print(f"The sum of the first {n} even numbers is = {total}")

input("Press Enter to exit")