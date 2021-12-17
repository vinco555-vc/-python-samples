import time
#Print 1 to 10
for i in range(10):
    print(i+1)

#Print a range of numbers
for i in range(50,60):
    print(i+1)

#Print a range incrementing by 2
for i in range(50,60,2):
    print(i+1)

#Print each letter in my name
for i in "Vinnie Coyle":
    print(i)

# Counter from 10 to 0,  happy newyear
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!!!")