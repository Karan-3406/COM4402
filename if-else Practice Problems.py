# 1. Cinema Ticket Category
age = int(input("Enter age: "))
if age < 5:
    print("Free entry")
elif age >= 5 and age < 18:
    print("Child ticket")
elif age >= 18 and age < 65:
    print("Adult ticket")
else:
    print("Senior ticket")

# 2. Library Fine Calculator
days_late = int(input("Enter days late: "))
if days_late <= 0:
    print("No fine")
elif days_late > 0 and days_late < 6:
    print("Fine = £1")
elif days_late >= 6 and days_late < 11:
    print("Fine = £5")
else:
    print("Fine = £10 and membership review")

# 3. Exam Borderline Check (Nested)
score = int(input("Enter Score (0 - 100): "))
if score >= 38:
    if score >= 38 and score <= 42:
        print("Borderline pass, consider review.")
    else:
        print("Clear pass.")
else:
    print("Fail.")

# 4. Discount Eligibility
is_student = input("Are you a student (yes/no): ")
age = int(input("Enter age: "))
if is_student == "yes" or age < 18:
    print("Discount applied")
else:
    print("No discount")

# 5. Traffic Light Action
colour = input("What colour (red/amber/green): ").lower()
if colour == "red":
    print("Stop")
elif colour == "amber":
    print("Get ready")
elif colour == "green":
    print("Go")
else:
    print("Invalid colour")

# 6. Multiple of 3, 5, or Both
number = int(input("Enter a number: "))
if (number % 3) == 0 and (number % 5) == 0 and number != 0:
    print("FizzBuzz")
elif (number % 3) == 0 and number != 0:
    print("Fizz")
elif (number % 5) == 0 and number != 0:
    print("Buzz")
else:
    print("No match")

# 7. Meal Recommendation (Nested)
time_of_day = input("What is the time of day? (Morning/Afternoon/Evening): ")
is_hungry = input("Are you hungry? (Yes/No)")
if is_hungry == "no":
    print("have some water and rest")
elif is_hungry == "yes":
    if time_of_day == "morning":
        print("Have breakfast")
    elif time_of_day == "afternoon":
        print("Have lunch.")
    elif time_of_day == "evening":
        print("Have dinner.")
    else:
        print("Snack time.")

# 8. Module Mark Status
coursework_mark = int(input("Enter coursework mark (0 - 100): "))
exam_mark = int(input("Enter exam mark (0 - 100): "))
if coursework_mark < 35 or exam_mark < 35:
    print("Automatic fail (component below 35)")
elif ((coursework_mark + exam_mark)/2) >= 40:
    print("Module passed.")
else:
    print("Module failed (average below 40).")

# 9. Simple Two-Stage Verification
pin = int(input("Enter pin: "))
if pin == 1234:
    answer = input("What is your favourite colour? ").lower()
    if answer == "blue":
        print("Access granted.")
    else:
        print("Security answer incorrect.")
else:
    print("Wrong PIN")

# 10. Sport Suggestion by Weather and Mood
weather = input("What is the weather? (Sunny/Rainy/Cold): ").lower()
mood = input("What is your mood? (Active/Tired): ").lower()
if weather == "sunny":
    if mood == "active":
        print("Go for a run")
    elif mood == "tired":
        print("Relax in the park")
elif weather == "rainy":
    print("Indoor workout")
elif weather == "cold":
    print("Go to the gym")

