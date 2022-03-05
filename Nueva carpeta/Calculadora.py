
# Online Python - IDE, Editor, Compiler, Interpreter

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operation = input("What operation do you want to perform? (addition, subtraction, multiplication, division")

if operation == "addition":
    print("This is the score of the addition: ", num_1 + num_2)
elif operation == "subtraction":
    print("This is the score of the subtraction: ", num_1 - num_2)
elif operation == "multiplication":
    print("This is the score of the multiplication: ", num_1 * num_2)
elif operation == "division":
    print("This is the score of the division: " , num_1 / num_2 )
else:
    print("Invalid input")
    
