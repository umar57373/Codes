def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error: Division by zero"
    return a/b

while True:
    print("1.addition\n"
    "2.Subraction\n"
    "3.Multiply\n"
    "4.Division\n"
    "5.Exit")
    case=int(input("Enter Your Choice: "))
    if case==1:
        a,b=map(int,input("Enter the Two Numbers: ").split())
        print(f"Result: {addition(a,b)}")
    elif case==2:
        a,b=map(int,input("Enter the Two Numbers: ").split())
        print(f"Result: {subraction(a,b)}")
    elif case==3:
        a,b=map(int,input("Enter the Two Numbers: ").split())
        print(f"Result: {multiply(a,b)}")
    elif case==4:
        a,b=map(int,input("Enter the Two Numbers: ").split())
        print(f"Result: {division(a,b)}")
    elif case == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice...")
