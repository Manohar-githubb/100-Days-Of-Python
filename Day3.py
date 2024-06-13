#conditional statements, Logical operoators, Code Blocks and scope, Name spacing and the project(game)


# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm?"))
# if height>=120:
#     print("you can ride the rollercoaster")
# else:
#     print("Sorry, you cannot ride...")

# number=int(input())
# if number%2 == 0:
#     print(f"The {number} is a even number")
# else:
#     print(f"The {number} is odd number")

# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm?"))
# if height>=120:
#     print("you can ride the rollercoaster")
#     age=int(input("What is your age?"))
#     if age<=18:
#         print("Ticket is $7 dollars")
#     else:
#         print("Ticket is $15 dollars")
# else:
#     print("Sorry, you cannot ride...")

# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm?"))
# if height>=120:
#     print("you can ride the rollercoaster")
#     age=int(input("What is your age?"))
#     if age<=12:
#         print("Ticket is $5 dollars")
#     elif age<=18:
#         print("Ticket is $7 dollars")
#     else:
#         print("Ticket is $15 dollars")
# else:
#     print("Sorry, you cannot ride...")

# height=float(input())
# weight=int(input())
# bmi=weight/height**2
# if bmi<18.5:
#     print(f"your bmi is {bmi},you are underweight")
# elif bmi<25:
#     print(f"your bmi is {bmi},you have normal weight")
# elif bmi<30:
#     print(f"your bmi is {bmi},you are slightly overweight")
# elif bmi<35:
#     print(f"your bmi is {bmi},you are overweight")
# else:
#     print(f"your bmi is {bmi},you are too heavy weight")
        

# year=int(input())
# if year%4==0:
#     if year%100==0:
#          if year%400==0:
#              print("leap year")
#          else:
#             print("not leap year")
#     else:
#         print("not leap year")
# else:
#     print("Not leap year")        

# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm?"))
# bill=0
# if height>=120:
#     print("you can ride the rollercoaster")
#     age=int(input("What is your age?"))
#     if age<=12:
#         bill=5
#         print("Ticket is $5 dollars")
#     elif age<=18:
#         bill=7
#         print("Ticket is $7 dollars")
#     else:
#         bill=12
#         print("Ticket is $12 dollars")
#     want_photo=input("Do yoy want a photo? y or n")
#     if want_photo=='y':
#         bill=bill+3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you cannot ride...")

# print("Thankyou for choosing pizza deliveries")
# size=input()
# add_perperoni=input()
# add_cheese=input()
# bill=0
# if size=='s':
#     bill+=15
# elif size=='m':
#     bill+=20
# else:
#     bill+=25
# if add_perperoni=='y':
#     if size=='s':
#         bill+=2
#     else:
#         bill+=3
# if add_cheese=='y':
#     bill+=1
# print(f"Your final bill is : {bill}")

print("The love calculator is calculating your score...")
name1=input()
name2=input()
combined_names=name1+name2
lower_names=combined_names.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
firsr_digit=t+r+u+e
l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit=l+o+v+e
score=(str(firsr_digit)+(second_digit))
print(score)

