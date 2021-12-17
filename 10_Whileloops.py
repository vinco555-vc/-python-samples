

#Enter name, if they do not enter name, then repeat until they do

from typing import DefaultDict


fname = ""
while len(fname) == 0:
    fname = input("What is your name : ")


#Using the none value
lname = None
while not(lname):
    lname = input("What is your last name : ")

print("Hello, " + fname + lname)
