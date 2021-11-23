n = 10
print("\n")
print('*'*500)
print("Welcome!, In this Game You can Choose A number and let your friend Guess It, in the Agreed No. of Attempts")
print('*'*500)
print("\n")
InputChoice = input("We have a pre-defined Value Also,if you want go ahead with Your Number, Just Press 'Y' ")
if (InputChoice == 'Y'):
    print("\n")
    n = int(input("Choose the NUmber You want Your Friend To  Guess! : "))
    print("Well Be clearing Your Screen Now! To Hide the Number from your Friend")
    print("\n"*50)
print('*'*700)
print("We have  cleared Your Screen Now! To Hide the Number from your Friend \nFollow The Scrren Instruction To play Now :")
print('*'*500)
print("\n")
Attempts = int(input("Enter the No Of Attempts You want : "))
AttemptsLeft = 0
while Attempts-AttemptsLeft > 0 :
    print("You have",Attempts-AttemptsLeft," Remaining Attempts!")
    Your_Try = int(input("Enter Your Guess : "))
    if(Your_Try > n):
        print("Try A samller Element ")
        AttemptsLeft += 1
    elif(Your_Try < n):
        print("Try a bigger Element ")
        AttemptsLeft += 1
    elif(Your_Try == n):
        print("Congrats!You guessed Right!")
        print("Great!You have Won in ",Attempts-AttemptsLeft," Remaining Attempts Left")
        break
    if(Attempts-AttemptsLeft == 0):
        print("Hard Luck!You have Exhausted All your Attempts!")
