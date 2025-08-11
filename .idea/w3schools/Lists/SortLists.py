
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)         # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

numlist = [5, 7, 9, 12, 3, 1]
numlist.sort()
print(numlist)          # [1, 3, 5, 7, 9, 12]

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)         # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


numlist = [5, 7, 9, 12, 3, 1]
numlist.sort(reverse = True)
print(numlist)          # [12, 9, 7, 5, 3, 1]
print("\n------------------------------------------------------------------------------------")


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first)

def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)         # [50, 65, 23, 82, 100]


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)         # ['Kiwi', 'Orange', 'banana', 'cherry']

# if you want a case-insensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort( key = str.lower)
print(thislist)         # ['banana', 'cherry', 'Kiwi', 'Orange']


# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)         # ['cherry', 'Kiwi', 'Orange', 'banana']