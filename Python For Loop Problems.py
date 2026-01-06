# 1. Repeat A Word
word = input("Enter word: ")
n = int(input("Enter number: "))
for i in range(n):
    print(f"{i + 1}: {word}")

# 2. Sum of First N Numbers
number = 0
n = int(input("Enter number: "))
for i in range(n):
    number = (i+1) + number
print(number)

# 3. Multiplication Table
x = int(input("Enter number: "))
for i in range(10):
    print(f"{i+1} x {x} = {(i+1)*x}")

# 4. Count Characters (Non-Space)
sentence = input("Enter sentence: ")
length = 0
for char in sentence:
    if char != " ":
        length = length + 1
print(length)

# 5. Find Maximum Mark
markNo = int(input("How many marks will you enter: "))
highestMark = 0
for i in range(markNo):
    mark = int(input("Enter number: "))
    if mark > highestMark:
        highestMark = mark
print(f"The highest mark is {highestMark}")

# 6. Filter Passing Marks
markNo = int(input("How many marks will you enter: "))
markList = []
passNum = 0
for i in range(markNo):
    mark = int(input("Enter number: "))
    if mark >= 40:
        markList.append(mark)
        passNum = passNum + 1
print(*markList,sep="\n")
print(f"Number of passes: {passNum}")

# 7. Reverse A String (Manual)
word = input("Enter a word: ")
reverseWord = ""
for char in word:
    reverseWord = char + reverseWord
print(reverseWord)

# 8. Count Specific Letter in a List of Names
nameList = []
nameNo = int(input("How many names will you enter: "))
for i in range(nameNo):
    nameList.append(input("Enter name: ").lower())
letter = input("Enter letter: ")
letterNo = 0
for i in nameList:
    if letter in i:
        letterNo += 1
print(letterNo)

# 9. Grade Statistics
markNo = int(input("How many marks will you enter: "))
markList = []
totalMarks = 0
averageCount = 0
distinctions = 0
for i in range(markNo):
    mark = int(input("Enter marks (0 - 100): "))
    totalMarks += mark
    averageCount += 1
    if mark >= 70:
        distinctions += 1
print(f"Total Marks: {totalMarks}")
print(f"Average Marks: {totalMarks/averageCount}")
print(f"Number of Distinctions: {distinctions}")

# 10. Simple Text-Based Bar Chart
numNum = int(input("How many numbers will you enter: "))
chartList = []
for i in range(numNum):
    chartList.append("*"*int(input("Enter number: ")))
print(*chartList,sep="\n")