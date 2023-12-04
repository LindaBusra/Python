#Lesson 04_09_2023

# dictionary {"nøkkel": verdi}

kontakter = {"Alice": "alice@example.com", "Bob": "bob@example.com", "Mike": "mike@example.com"}
print(kontakter)
print(kontakter.values())
print(kontakter.keys())

print(kontakter.get("Alice"))       #it gets value of "Alice"
print(kontakter)
kontakter.pop("Alice")      #remove the item which key value is "Alice"
print(kontakter)


print("-----------------------------------------------")



kontakter = {"Alice":
                 {"personnumber":"123456789",
                  "navn":"Alice Emily",
                  "tlf":"2222222222"},
             "Bob":
                 {"personnumber":"123456788",
                  "navn":"Bob Nilsen",
                  "tlf":"3333333333"},
                                        }
print(kontakter.get("Bob"))



#create en dictionary:
person= {}

person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['email'] = input("Enter your email: ")
print(person)



#liste in dictionory
favorite_places = {"Alice": ["Nature", "School", "Home"],
                   "John": ["Home", "Work", "Gym"]}

for key, value in favorite_places.items():
    print(f"\n{key.title()} like the following places:")
    for i in value:
        print(f"-{i.title()}")



dic = {"navn": "Jo", "alder":25}
print(dic["navn"])      #Jo
print(dic["alder"])     #25
