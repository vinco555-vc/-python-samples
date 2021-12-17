
dishes = {"bowl", "plate", "cup", "knife"}
utensils = {"fork", "spoon", "knife"}

print("Dishes : " + str(dishes))
print("Utensils : " + str(utensils))

#add
utensils.add("napkin")
#Remove
utensils.remove("fork")

print("Dishes : " + str(dishes))
print("Utensils : " + str(utensils))

#utensils.clear()

#Add a set to another set
dishes.update(utensils)
print("Dishes After update: " + str(dishes))

dishes.remove("spoon")
dishes.remove("napkin")

print("Dishes : " + str(dishes))
print("Utensils : " + str(utensils))

#create new set from 2 sets
dinner_table = utensils.union(dishes)

print("differences between sets : " + str(dishes.difference(utensils)))
print("Items in both sets : " + str(utensils.intersection(dishes)))

#loop around set
for x in utensils:
    print(x)