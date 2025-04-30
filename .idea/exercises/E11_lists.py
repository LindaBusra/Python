
#Lists

"""Unpack a Collection
If you have a collection of values in a list,
Python allows you to extract the values into variables. This is called unpacking."""

fruits = ["apple", "orange", "cherry"]
x,y,z = fruits
print(x, y, z)
print(x)



fav_movies = [1,5,7,3,4.6, True, "Hello"]
print(fav_movies)

fav_numbers = [4,9,33]
print(fav_numbers[1])
print(len(fav_numbers))


fav_movies= ["Sandlot", "The Lego Movie", "Dune"]

print(fav_movies)
print(fav_movies[0])
print(len(fav_movies))
fav_movies.append("Iron Man")
print(len(fav_movies))

#put an itemin a specific plass
fav_movies.insert(1,"Batman")
print(fav_movies)

#delete an item
del(fav_movies[2])
print(fav_movies)

#Remove enough items from fav_movies until there is only one movie left
del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
print(fav_movies)


print("---------------------------------------------------------------------")


numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Veli", "Ayşe"]
mixed = [1, "Python", True]

print(numbers[0])    # it prints first element
print(len(numbers))  # it prints length

print(mixed[1])         #Python
print(len(mixed))       #3


print("---------------------------------------------------------------------")



#Find the max number in this array
numbers = [10, 5, 20, 8, 15]
max_number = max(numbers)
min_number = min(numbers)
print("The max number is: ", max_number)
print("The min number is: ", min_number)