
# Online Python - IDE, Editor, Compiler, Interpreter

def addition (x,y):
    """This function addition two numbers"""
    return x + y
def subtraction (x,y):
    """This function subtraction two numbers"""
    return x - y
def multiplication (x,y):
    """This function multiplication two numbers"""
    return x * y
def division (x,y):
    """This function division two numbers"""
    return x/y

def power(x,y):
    """This gives power"""
    
    return pow(x,Y)
    
 #Take input from user
print("Select an option: ")
print("1.Addition")
print("1.Subtraction")
print("1.Multiplication")
print("1.Division")
print("1.Power")
choice=input("Enter choice 1/2/3/4/5: ")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
    
if choice == "1":
    print(num_1, "+", num_2,"=", addition(num_1,num_2))
elif choice == "2":
    print(num_1, "-", num_2,"=", subtraction(num_1,num_2))
elif choice == "3":
    print(num_1, "*", num_2,"=", multiplication(num_1,num_2))
elif choice == "4" :
    print(num_1, "/", num_2,"=", division(num_1,num_2))
elif choice == "5" :
    print(num_1, "^", num_2, "=", power (num_1,num_2))
else:
    print("Invalid input")
