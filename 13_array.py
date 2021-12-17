#Create a list
food = ["Pizza", "Hamburger", "Hotdog", "Spaghetti", "Pudding"]

food[0] = "sushi"

food.append("Ice-creame") #Add to end
food.remove("Hotdog") #Remove an item
food.pop() #
food.insert(0, "Cake") #Insert an item
food.sort() #Sort list
food.clear() #Clear list

for x in food:
    print(x)