# File Concepts

#To open and read the text in the file
# file = open("my_file.txt")
# contents=file.read()
# print(contents)
# file.close()
         #OR
# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)

#To add or append the text with already entered text in the file
# with open("my_file.txt","a") as file:  
#     file.write("\nMy new text")

#To open a new file and write in that file
# with open("new_file.txt","w") as file:  
#     file.write("My new text")
    
#We can also specify the path to the file we want to read or write
with open("/Users/manoh/OneDrive/Desktop/100daysofcode/new_file.txt") as file:   #we can also specify path using backword slashes in python
    contents=file.read()
    print(contents)