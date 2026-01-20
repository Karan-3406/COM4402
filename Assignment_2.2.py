menuChoice = 0
bestScore = 0
currentScore = 0

# Questions for Quiz
quizQuestions = [
    {
        "question": "What do bees make?",
        "options": ["Honey", "Apple Juice", "Chocolate", "Chicken"],
        "correctOption": 1,
        "type": "multiple"
    },
    {
        "question": "What animal is known to meow",
        "correctOption": "cat",
        "type": "text"
    },
    {
        "question": "What shape has three sides?",
        "options": ["Circle", "Triangle", "Square", "Pentagon"],
        "correctOption": 2,
        "type": "multiple"
    },
    {
        "question": "What animal is known to moo",
        "correctOption": "cow",
        "type": "text"
    },
    {
        "question": "What is the name given to frozen water?",
        "options": ["Stone", "Sand", "Ice"],
        "correctOption": 3,
        "type": "multiple"
    },
    {
        "question": "Which animal is the only mammal that can fly?",
        "options": ["Penguin", "Bumble Bee", "Eagle", "Bat", "Butterfly"],
        "correctOption": 4,
        "type": "multiple"
    },
    {
        "question": "What is the largest land animal",
        "options": ["Saltwater Crocodile", "Giraffe", "Blue Whale", "African Bush Elephant", "Ostrich"],
        "correctOption": 4,
        "type": "multiple"
    }
]

# if question is multiple choice do
def get_integer(start_value, end_value):
    while True:
        try:
            user_input = int(input(f"Enter value between {start_value} and {end_value}: "))

            if start_value <= user_input <= end_value:
                return user_input
            else:
                print(f"Error: Number must be between {start_value} and {end_value}.")

        except ValueError:
            print("Error: Please enter a valid integer.")

# if question is text do
def get_text():
    while True:
        # try:
        user_input = input(f"Enter Answer: ").lower()

        if user_input != "":
            return user_input
            break
        else:
            print(f"Error: Input cannot be empty.")

def handle_multiple_choice_question(question, current_score):
    print(question["question"])

    optionNumber = 1
    for option in question["options"]:
        print(optionNumber, "-", option)
        optionNumber = optionNumber + 1

    userChoice = get_integer(1, len(question["options"]))

    updated_score = current_score + 1 if check_answer(userChoice, question["correctOption"]) else current_score
    return updated_score

def handle_text_question(question, current_score):
    print(question["question"])

    userChoice = get_text()

    updated_score = current_score + 1 if check_answer(userChoice, question["correctOption"]) else current_score
    return updated_score


def check_answer(user_input, stored):
    # Check if user answer is correct
    if user_input == stored:
        print("Correct\n")
        return True
    else:
        print("incorrect\n")
        return False

quizCompleted = False

# Main Code
# Display Start Menu
print("MENU\n")

menuChoice = input("0 - Exit\n1 - Start Quiz\n2 - Show Previous Score\n\nInput: ")

if menuChoice.isdigit():
    menuChoice = int(menuChoice)
else:
    print("Enter Integer")

while menuChoice != 0:
    if menuChoice == 1:
        # Choice 1 = Display Quiz
        userChoice = 0
        print()

        for question in quizQuestions:
            if question["type"] == "multiple":
                currentScore = handle_multiple_choice_question(question, currentScore)
            elif question["type"] == "text":
                currentScore = handle_text_question(question, currentScore)

        print("You finished the quiz")
        print(f"You scored {currentScore} out of {len(quizQuestions)}")

        if currentScore > bestScore:
            bestScore = currentScore

        quizCompleted = True
        previousScore = currentScore

    elif menuChoice == 2:
        # Choice 2 - Display Previous Score
        if quizCompleted:
            print(f"Previously, you scored {currentScore} out of {len(quizQuestions)}")
            print(f"Your best score is {bestScore} out of {len(quizQuestions)}")
        else:
            print("You have not previously completed this quiz")

    else:
        print("Invalid Input")

    print("\nMENU\n")
    menuChoice = input("0 - Exit\n1 - Start Quiz\n2 - Show Previous Score\n\nInput: ")
    if menuChoice.isdigit():
        menuChoice = int(menuChoice)
    else:
        print("Enter Integer")