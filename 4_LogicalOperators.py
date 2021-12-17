temp = int(input("What is the temperture outside"))

if temp >= 0 and temp <= 30:
    print("The temp is good today")
    print("go Outside")
elif temp < 0 or temp > 30:
    print("The temp is bad today")
    print("Stay inside")

#Not operator - Reverse the output, if true then changes to false
if not(temp >= 0 and temp <= 30):
    print("The temp is bad today")
    print("Stay inside")
elif not(temp < 0 or temp > 30):
    print("The temp is good today")
    print("go Outside")
    
