#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default
#To sort descending, use the keyword argument reverse = True
#By default the sort() method is case sensitive

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)         #['banana', 'kiwi', 'mango', 'orange', 'pineapple']


#if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)         #['banana', 'cherry', 'Kiwi', 'Orange']


#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)         #['pineapple', 'orange', 'mango', 'kiwi', 'banana']



#Sort the list numerically:
numList = [5, 10, 25, 9, 45]
numList.sort()
print(numList)          #[5, 9, 10, 25, 45]


#Sort the list descending:
numList = [5, 10, 25, 9, 45]
numList.sort(reverse=True)
print(numList)          #[45, 25, 10, 9, 5]


#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?"
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)         #['cherry', 'Kiwi', 'Orange', 'banana']


#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first)

#Sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)         #[50, 65, 23, 82, 100]