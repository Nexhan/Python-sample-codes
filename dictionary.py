#Beginner python cheetsheat for dictionaries in python

# Synonyms dictionary
Synonyms = {
    "hungry":"ravenous", 
    "weed":"Marijuana",
    "rice":"corn"}

#Assigning values
#using key to get the values
print(Synonyms["hungry"])

#Adding new key-value pairs
Synonyms["burger"] = "Sandwich"
print(Synonyms)

#modifying values
Synonyms["weed"]= "gANJA"
print(Synonyms)

#deleting key-value pair
del Synonyms['weed']
print(Synonyms)

#looping through a dictionary.

for name_one, name_two in Synonyms.items():
    print(f"{name_one}:{name_two}")

for name_one in Synonyms.keys():
    print(name_one)

for name_two in Synonyms.values():
    print(name_two)

# sorting dictionaries into list:

# nesting
# storing set of dictinaries into list

cars = []

lambo_dict = {
    "lambo": "red",
    "speed": 200,
    "mileage" : 20
}

cars.append(lambo_dict)

ferrari_dict = {
    "Ferrari": "Blue",
    "speed" : 150,
    "mileage": 27
}

cars.append(ferrari_dict)

print(cars)

for car in cars:
    for spec, info in car.items():
        print(f"{spec}:{info}")
    print("\n")


lambo_dict = {
    "lambo": ["red","blue"],
    "speed": str(200),
    "mileage" : ["Highway=20", "city= 15"],
    }


for spec, info in lambo_dict.items():
    print(f"{spec}:")
    for information in info:
        print(information)
    
    