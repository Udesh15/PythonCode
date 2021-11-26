while True :
    try:
     N = int(input("Enter the digit :"))
     M = int(input("Enter the digit :"))
     M+N
    except ValueError as  E:
     print(E)
     break

# while True:
#     try:
#        x = int(input("Please enter a number: "))
#        break
#     except ValueError:
#        print("Oops!  That was no valid number.  Try again...")