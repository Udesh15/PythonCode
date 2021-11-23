#User input for Dictionary
Dic = {}
for i in range(2):
    Keys = input("enter the key for Dic")
    values = input("enter the value")
    Dic[Keys]=values
print(Dic.values())
print(Dic.keys())