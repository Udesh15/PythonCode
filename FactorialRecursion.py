def Factorial(N,Fact):
    #N = int(input("Enter the Value for factorial : "))
    #Fact = 1

    #print(N)
    Fact = N * Fact
    N -= 1
    #print(N)
    if N > 0:
        Factorial(N,Fact)
    else:
        print(Fact)


#N = print(int(input("Enter the value Of N : ")))
#Fact = print(int(input("Enter the value Of Fact : ")))
Factorial(5,1)






