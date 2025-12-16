# 1. Receipt with Formatting
item_name = input("Enter item name: ")
price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity: "))
print(f"You bought {quantity} x {item_name} at £{price} each. Total = £{price*quantity}")

# 2. Age Description
age = int(input("Enter your age: "))
print("You are",age,"years old.")
print(f"You are {age} years old")

# 3. Tidy Name & Course
full_name = input("Enter full name: ").strip()
course_name = input("Enter course name: ").strip().upper()
print(full_name)
print(course_name)

# 4. Multi-line Details with \n
full_name = input("Enter full name: ").strip()
age = int(input("Enter your age: "))
course_name = input("Enter course name: ").strip().upper()
print(f"{full_name}\n{age}\n{course_name}")

# 5. Message Customiser with .replace()
template = ("Hello NAME, welcome to COURSE.")
name = input("Enter name: ")
course_name = input("Enter course name: ").strip().upper()
template = template.replace("NAME",name).replace("COURSE",course_name)
print(template)

# 6. Shouting and Whispering
sentence = input("Enter a sentence: ")
print (f"{sentence.upper()}\n{sentence.lower()}\n{len(sentence)}")

# 7. Safe Division with Message
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 == 0:
    print("Error: cannot divide by zero")
else:
    print(f"{num1} divided by {num2} is {num1/num2}")

# 8. Login Name Normaliser
username = input("Enter username: ").strip().lower()
print(username) #this is useful for usernames so two users don't have the same username with different cases

# 9. Personalised Letter (Basic)
name = input("Enter name: ").strip()
age = int(input("Enter your age: "))
course_name = input("Enter course name: ").strip()
print(f"""Hello, {name}
you are {age} years old
and you are in the {course_name.upper()} course""")

# 10. Style Comparison Exercise
name = "Sam"
age = 19
course = "COM4402"
print("Hello "+name+", you are "+str(age)+" and enrolled in "+course)
print("Hello",name," you are",str(age),"and enrolled in",course)
print(f"Hello {name}, you are {str(age)} and enrolled in {course}")