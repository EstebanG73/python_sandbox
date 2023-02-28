#Practicing with while
a = 1
wt= 0
while a == 1:
    w = float(input("Enter student weight = "))
    wt += w
    a = int(input("Another student? 0:no 1:yes: "))

print("Total weight = ", wt)

input("Press Enter to exit")

