def addition(a, b):
    c = a + b
    return (c)
    # print(c)

def subtraction(a, b):
    c = b - a
    return (c)

def multiplication(a, b):
    c = a * b
    return (c)

def division(a, b):
    c = a/b
    return (c)

def OperationAsperUser():
    a = int(input("Enter the value of 1st Element : "))
    b = int(input('Enter the value of 2nd Element : '))
    print(
        "Hello! These are the Possible Operations, Enter the Symbol as Specified :  \n Addition : + \n Subraction : - \n Division : / \n Multiply : *")
    Opera = input("Enter the operation you want to do : ")
    if Opera == '+':
        c = addition(a, b)
        print(c)
        Rerun()
    elif Opera == '-':
        c = subtraction(a, b)
        print(c)
        Rerun()
    elif Opera == '*':
        c = multiplication(a, b)
        print(c)
        Rerun()
    elif Opera == '/':
        c = division(a, b)
        print(c)
        Rerun()

def Rerun():
    RunAgain = input("If You want to do Any otherOperation Press 'Y', Else Press Enter to exit ")
    if RunAgain == 'Y' :
        OperationAsperUser()
    print("Thank You For Using the Calculator!")


OperationAsperUser()







