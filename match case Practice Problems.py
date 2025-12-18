# 1. Cinema Ticket Category
age = int(input("Enter age: "))
match age:
    case age if age < 5:
        print("Free entry")
    case age if age >= 5 and age < 18:
        print("Child ticket")
    case age if age >= 18 and age < 65:
        print("Adult ticket")
    case _:
        print("Senior ticket")

# 2. Library Fine Calculator
days_late = int(input("Enter days late: "))
match days_late:
    case days_late if days_late <= 0:
        print("No fine")
    case days_late if days_late > 0 and days_late < 6:
        print("Fine = £1")
    case days_late if days_late >= 6 and days_late < 11:
        print("Fine = £5")
    case _:
        print("Fine = £10 and membership review")

# 3. Traffic Light Action
colour = input("What colour (red/amber/green): ").lower()
match colour:
    case colour if colour == "red":
         print("Stop")
    case colour if colour == "amber":
        print("Get ready")
    case colour if colour == "green":
         print("Go")
    case _:
        print("Invalid colour")

# 4. Multiple of 3, 5, or Both
number = int(input("Enter a number: "))
match number:
    case number if (number % 3) == 0 and (number % 5) == 0 and number != 0:
        print("FizzBuzz")
    case number if (number % 3) == 0 and number != 0:
        print("Fizz")
    case number if (number % 5) == 0 and number != 0:
        print("Buzz")
    case _:
        print("No match")

# 5. Module Mark Status
coursework_mark = int(input("Enter coursework mark (0 - 100): "))
exam_mark = int(input("Enter exam mark (0 - 100): "))
match coursework_mark:
    case coursework_mark if coursework_mark < 35 or exam_mark < 35:
        print("Automatic fail (component below 35)")
    case coursework_mark if ((coursework_mark + exam_mark)/2) >= 40:
        print("Module passed.")
    case _:
        print("Module failed (average below 40).")

# 6. Shape Area Calculator
shape = input("Enter shape? (Circle, Square, Triangle, Rectangle) ").lower()
match shape:
    case "circle":
        radius = int(input("Input radius: "))
        print(radius * radius * 3.14)
    case "square":
        base = int(input("Enter base: "))
        print(base^2)
    case "triangle":
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        print(base * height / 2)
    case "rectangle":
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        print(base * height)
    case _:
        print("Invalid Input")



