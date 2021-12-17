
#Break
while True:
    name = input("Enter your name : ")
    if name != "":
        break
print("Your name is : " + name)

#contine - remove dashes from phone number
phone_number = "123-456-7890"
for i in phone_number:
    if i == '-':
        continue
    print(i, end="")
print()

#pass
for i in range(1, 21):
    if(i == 13):
        pass
    else:
        print(str(i) + " ", end="")
print()