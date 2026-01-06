# 1. Countdown to Launch
num = int(input("Enter a starting number: "))
while num >= 1:
    print(num)
    num -= 1
print("Lift Off!")

# 2. Sum Until Zero (Sentinel)
totalNum = 0
while True:
    num = int(input("Enter integer: "))
    totalNum += num
    if num == 0:
        break
print(totalNum)

# 3. Password Checker (Do-While)
correct_password = "python123"
while True:
    attempt = input("Enter Password: ")
    if attempt == correct_password:
        print("Access Granted")
        break
    else:
        print("Try Again")

# 4. Guess the secret number
secret = 17
while True:
    guess = int(input("Guess: "))
    if guess == secret:
        print("Well Done")
        break
    elif guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")

# 5. Menu Loop - Simple Calculator
while True:
    menuChoice = int(input("\n1. Add\n2. Subtract\n0. Exit\n\n"))
    if menuChoice == 0:
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if menuChoice == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif menuChoice == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        print("Invalid Input")

# 6. Input Validation (Positive Integer)
while True:
    num = int(input("Enter number: "))
    if num <= 0:
        print("Error, Try Again")
    else:
        print("You Entered:",num)
        break

# 7. Average of Marks Until -1
markCount = 0
totalMarks = 0
while True:
    mark = int(input("Enter marks (0 - 100): "))
    if mark == -1:
        print(f"Marks entered: {markCount}")
        print(f"Average: {totalMarks/markCount}")
        break
    else:
        markCount += 1
        totalMarks += mark

# 8. Limited Login Attempts
username = "Edwin67"
password = "password"
count = 0
while True:
    if count >= 3:
        print("Account Locked")
        break
    username_input = input("Enter Username: ")
    password_input = input("Enter Password: ")
    if username_input == username and password_input == password:
        print("Login Successful")
        break
    elif username_input == username or password_input == password or count < 3:
        print("Invalid Credentials")
        count += 1

