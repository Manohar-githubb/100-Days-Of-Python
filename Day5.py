#loops and password generator project

# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")
#     print(fruits)
# print(fruits)

# stud_heights=input().split()
# for n in range(0,len(stud_heights)):
#     stud_heights[n]=int(stud_heights[n])
# print(stud_heights)

# stud_scores=input().split()
# for n in range(0,len(stud_scores)):
#      stud_scores[n]=int(stud_scores[n])
# highest_score=0
# for scores in stud_scores:
#     if scores>highest_score:
#         highest_score=scores
# print(f"The highest score is : {highest_score}")

# for num in range(1,10):
#     print(num)

# for num in range(1,10,2):
#     print(num)

# total = 0
# for num in range(1,101):
#     total=total+num
# print(f"Sum = {total}")

# target=int(input())
# even_sum=0
# for num in range(2,target+1,2):
#     even_sum+=num
# print(even_sum)

#FizzBuzz Game
# target=100
# for num in range(1,target+1):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)

#PASSWORD GENERATOR
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")