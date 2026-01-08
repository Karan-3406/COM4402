# 1. Right-Angled Triangle of Stars
for i in range(5):
    for j in range(0,i+1):
        print("*", end = "")
    print()

# 2. Number Triangle (Row Number)
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{i}", end = "")
    print()

# 3. Increasing Number Triangle
num = 0
for i in range(1,5):
    for j in range(1,i+1):
        num += 1
        print(f"{num}", end = "")
    print()

# 4. Square Multiplication Grid
for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j}", end = " ")
    print()

# 5. Coordinate Grid
for i in range(0,3):
    for j in range(0,4):
        print(f"({i},{j})", end = " ")
    print()

# 6. Hollow Square of Stars
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1:
            print(f"*", end = "")
        elif j == 0 or j == 1:
            print("*", end = " "*(size-2))
    print()

# 7. Centered Pyramid of Stars
size = 4
for i in range(0,size):
    print(end=" "*(size-i))
    for j in range(0,i+1):
        print("*", end = "")
    print(end="*"*i)
    print()

# 8. Times Table Block (2–4 by 1–5)
for i in range(5):
    for j in range(3):
        print(f"{j + 2} x {i + 1} = {(j+2)*(i+1)}", end = "     ")
    print()

# 9. Checkerboard Pattern
halfSize = 4
for i in range(halfSize*2):
    for j in range(halfSize):
        if (i%2 == 0):
            print(f"#", end = ".")
        else:
            print(f".", end = "#")
    print()

# 10. Pascal-like Triangle (Simple Sums)
size = 5
for i in range(size):
    num = 1
    for j in range(i+1):
        print(num, end = " ")
        num = int(num * (i - j) / (j + 1))
    print()