#MAKING A LIST

bikes = ['Honda','yamaha','kawasaki','ktm','ninja']

#Accessing the elemets
first_bike = bikes[0]
second_bike = bikes[1]
print(first_bike)
print(second_bike)

#Negtive Index refers to items at the end of the list

print(bikes[-1])

#changing the elements
bikes[0] = 'tuktuk'
print(bikes)

# adding the elements

bikes.append('honda')
print(bikes)

#adding elemets in particular position

bikes.insert(0, 'VR')
print(bikes)

#removing elements by its position and value

# by position
del bikes[0]
#by value
bikes.remove('tuktuk')
print(bikes)

#poping elemets
pop_lastelement = bikes.pop()
print(pop_lastelement)
specific_element= bikes.pop(1)
print(specific_element)

#length of a list
length = len(bikes)
print(length)

# sorting a list permanently
# sorting in ascending way
bikes.sort()
print(bikes)

#sorting in reverse order alphabetically

bikes.sort(reverse=True)

print(bikes)

# sorting a list temporarily

print(sorted(bikes))

bikes.reverse()
print(bikes)

for bike in bikes:
    print(bike)

for bike in bikes:
    print(f"welcome {bike}")

print("Welcome bike")

numbers = [1,2,3,4,5,6,7,8,]
print(numbers[-5:])