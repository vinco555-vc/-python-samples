name = "Vinnie Coyle"

#Get one char from string
fchar = name[0]
print(fchar)

#Use index to get multiple chars from string

#Print First name
first_name = name[0:7]
print(first_name)

#Print last name
last_name = name[7:len(name)]
print(last_name)

#Step over chars
fucky_name = name[0:len(name):2]
print(fucky_name)

#Reverse String - By not adding the start and end values, 0 and name.len is assumed
reverse_name = name[::-1]
print(reverse_name)

website = "http://google.com"
website2 = "http://yahoo.com"

#Create a slice object, removing from the start
slice = slice(7,-4)

print(website[slice])
print(website2[slice])