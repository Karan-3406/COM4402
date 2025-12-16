# 1. Simple Greeting
name = input("Enter your name: ")
print ("Hello", name)

# 2. Name and Age Sentence
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print ("Hello", name,"and you are", age ,"years old.")

# 3. Age Next Year
age = int(input("Enter your age: "))
age_next_year = age + 1
print ("Next year you will be",age_next_year)

# 4. Simple Two-Number Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
product = num1 * num2
print("Sum is",sum)
print("Product is",product)

# 5. Dynamic Typing with x
x = 10
print(x)
print(type(x))
x = "hello"
print(x)
print(type(x))

# 6. Fix the Type Confusion Bug
age = int(input("Enter age: "))
age_next_year = age + 1
print(age_next_year)

# 7. Naming Variables – Make It Clear
num1 = 50
num2 = 60
sum = num1 + num2
print(sum)

# 8. User Profile Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
age_next_year = age + 1
print ("Hello", name)
print ("Next year you will be",age_next_year)
print ("Your height is",height,"metres")
print(type(age),type(height))

# 9. Product Cost Calculator
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total_cost = price * quantity
print("You bought",quantity,"of",product_name)
print("Total cost is",total_cost)

# 10. Spot the Problems
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age_next_year = age + 1
print("hello", name, "next year you will be", age_next_year)
