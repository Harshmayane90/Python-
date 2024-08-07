
def choice():
    print("---------------")
    print(1, "Addition")
    print(2, "Subtraction")
    print(3, "Multiply")
    print(4, "Divide")
    print(5, "Exit")
    print()
# def calculate():
#     for n in range(1,10):
#         print(n)
# calculate()
    
first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))

def add():
    z= first- second
    print("Addition of the numbers is:",z)

def sub():
    z = first- second
    print("Subtraction of the numbers is:", z)

def mul():
    z = first *second
    print("Multiplication of the numbers is:", z)

def div():
    z = first/second
    print("Division of the numbers is:", z)

def exit_program():
    print("---------Exited-----------")
def display():
    while True:
        choice()
        ch = int(input("Enter your choice: "))
        if ch == 1:
            add()
        elif ch == 2:
            sub()
        elif ch == 3:
            mul()
        elif ch == 4:
            div()
        elif ch == 5:
            exit_program()
            break
        else:
            print("----------Invalid choice-----------")
            break
display()


