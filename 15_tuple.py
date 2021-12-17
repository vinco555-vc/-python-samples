student = ("Vinnie", 21, "male")


print("How many times 'Vinnie' appears in tuple : " + str(student.count("Vinnie")))
print("'male' is located at index : " + str(student.index("male")))

#Print content of student via loop
for x in student:
    print(x)

#Check to see if value is stored in tuple
if "Vinnie" in student:
    print("Vinnie is here")