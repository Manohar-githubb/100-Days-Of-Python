#Dictionaries and nesting

# prog_dict = {
#     "Bug" : "Its an error.",             #here, bug is a key and its value in the followed quotes
#     "Function" : "A piece of code",
#     123 : "Its a number"
# }
# print(prog_dict["Bug"],prog_dict[123])   #Retriving the items from the dictionary

#Adding new item in the dictionary
# prog_dict["Loop"] = "The action of doing something"
# print(prog_dict)

#create an empty dictionary.
# empty_dict = {}

#wipe an existing dictionary
# prog_dict = {}
# print(prog_dict)

#Edit an item in a dictionary
# prog_dict["Bug"] = "A moth in your computer."
# print(prog_dict)

#Loop through a dictionary
# for key in prog_dict:
#     print(key)
#     print(prog_dict[key])

#Nesting
# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin"
# }
#nesting a list in a dictionary
# travel = {
#     "France" : ["Paris","Lille","Dijon"]   #nesting dictiony with list
# }
# print(travel)

# travel = {
#     "France" : {"cities_visited": ["Paris","Lille","Dijon"], "total": 5}    #nesting dict with list inside another dictionary
# }
# print(travel)

#we can also nest inside a lists too like: 
# travel = [
#     {
#         "country" : "India",
#         "places" : ["Karnataka","Andhra","Mumbai"],
#         "total" : 12
#     }
# ]
# print(travel)