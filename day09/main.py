
#* Dictionary n Nest

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#*Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing somthing over and over again."

#*Create an empty dictionary
# empty_dictionary = {}

#*Wipe an existing dictinoary
# programming_dictionary = {}
# print(programming_dictionary["Bug"])

#*Edit an item in a dictionary
# programming_dictionary["Bug"] = "Fuck U"
# print(programming_dictionary["Bug"])

#*Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#*Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#*Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#*Nesting dictionary in a dictionary
travel_log = {
    "France": {"cities_visited:"["Paris", "Lille", "Dijon"], "total_visites: 12"},
    "Germany": {"cities_visited:"["Berlin", "Hamburg", "Stuttgart"], "total_visites: 9"}
}

#*Nesting Dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 9
    }
    
]