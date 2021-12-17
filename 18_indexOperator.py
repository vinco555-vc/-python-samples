name = "vinnie Coyle"

if(name[0].islower ):
    name = name.capitalize()
    print(name)
    print('Lower Case')
else:
    print('Upper Case')

fname = name[0:6].upper()
print(fname)

lname = name[7:].upper()
print(lname)

last_char = name[-1]
print(last_char)