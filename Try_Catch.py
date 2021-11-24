try :
    Value1 = int(input("This is a variable"))
    Value2 = int(input("This is 2nd variable"))
except Exception as E:
    print(E)
print("This should Run irrespective of above error")

#The Eception is catched rather than aborting the programme