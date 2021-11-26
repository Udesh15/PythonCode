while True :
    try:
     N = int(input("Enter the digit :"))
     M = int(input("Enter the digit :"))

    except ValueError as  E:
     print(E)
     #break
    else:
       M =  M + N
       print(M)
    break

# while True:
#     try:
#        x = int(input("Please enter a number: "))
#        break
#     except ValueError:
#        print("Oops!  That was no valid number.  Try again...")