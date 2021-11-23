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
    c = b / a
    return (c)

def OperationAsperUser():
    a = int(input())
    b = int(input())
    Opera = input("Enter the operation you want to do : ")
    if Opera == 'addition':
        c = addition(a, b)
        print(c)
    elif Opera == 'subtraction':
        subtraction(a, b)
    elif Opera == 'multiply':
        multiplication(a, b)
    elif Opera == 'division':
        division(a, b)

OperationAsperUser()





