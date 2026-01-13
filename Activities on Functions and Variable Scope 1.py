# Activity 1 – Fix the Greeting - Version A
def greet():
    message = "Hello from the function"
    return message
message = greet()
print(message)

# Activity 1 – Fix the Greeting - Version B
def greet():
    message = "Hello from the function"
    print(message)
greet()

# Activity 2 – Local vs Global Guess
count = 0
def add_one(count):
    count = count + 1
    print("Inside:", count)
    return count
count = add_one(count)
print("Outside:", count)

# Activity 3 – Complete the Function
def area_of_rectangle(width, height):
    area = width * height
    return area
w = float(input("Enter width: "))
h = float(input("Enter height: "))
print(f"Area is {area_of_rectangle(w,h)}")

# Activity 4 – Parameter vs Global - Version 1
rate = 0.2
def calculate_tax(amount):
    return amount * rate
print(calculate_tax(4))

# Activity 4 – Parameter vs Global - Version 2
def calculate_tax(amount, rate):
    return amount * rate
print(calculate_tax(4,0.2))

# Activity 5 – Bug Hunt: Discount Function
def apply_discount(price):
    discount = 0
    if price > 100:
        discount = 10
    final_price = price - discount
    return final_price
p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)

# Activity 6 – ATM Helper Functions
def show_menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice

def deposit(balance):
    amount = float(input("Amount to deposit: "))
    if amount > 0:
        balance += amount
    else:
        print("Error")
    return balance

def withdraw(balance):
    amount = float(input("Amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
    else:
        print("Error")
    return balance

balance = 0
while True:
    choice = show_menu()
    if choice == "0":
        print(f"Current Balance: {balance}")
        break
    elif choice == "1":
        balance = deposit(balance)
    elif choice == "2":
        balance = withdraw(balance)

# Activity 7 – Scope Explanation in Comments
total = 0
def add_mark(mark, total):
    total = total + mark
    return total
mark1 = int(input("Enter mark 1: "))
total = add_mark(mark1, total)
mark2 = int(input("Enter mark 2: "))
total = add_mark(mark2, total)
print("Total:", total)

# Activity 8 – Rewrite Using Functions
def get_user_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def print_message(name, age):
    if age >= 18:
        print(f"Hello {name}, you are an adult.")
    else:
        print(f"Hello {name}, you are under 18.")

name, age = get_user_details()
print_message(name, age)

# Activity 9 (Medium) – Login + Scope

def check_password(input_password):
    password = "pass1234"
    if input_password == password:
        return True
    else:
        return False

def login():
    user_password = input("Password: ")
    if check_password(user_password) == True:
        print("Welcome")
    else:
        print("Access Denied")

login()

# Activity 10 (Medium) – Refactor Parking Time Calculator
def convert_minutes(minutes):
    hours = minutes // 60
    remaining = minutes % 60
    return hours, remaining
def print_time(hours, remaining):
    if hours > 0 and remaining > 0:
        print(f"{hours} hour(s) and {remaining} minute(s)")
    elif hours > 0:
        print(f"{hours} hour(s)")
    else:
        print(f"{remaining} minute(s)")

hours, remaining = convert_minutes(int(input("Enter total parking minutes: ")))
print_time(hours, remaining)
