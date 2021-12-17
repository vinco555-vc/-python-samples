capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

#Add a new item to dictionary
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})

#Revmove item
capitals.pop('China')

#print each capital
for key,value in capitals.items():
    print(key,value)

#capitals.clear()

print(capitals.get('USA'))
