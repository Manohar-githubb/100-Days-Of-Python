# Debugging - 1.Describe the Problem
# def my_function():
#     for i in range(1,21):      #if range is 20, o/p is nothing
#         if i == 20:
#             print("You got it")
# my_function()

#2.Reproduce the Bug
# from random import randint
# dice_img = ["1","2","3","4","5","6"]
# dice_num=randint(0,5)                 #if randint range is (1,6), when 6 appears it shows error because list will count from 0 to 5th location. No 6th location present here.
# print(dice_img[dice_num])

#3.Play Computer 
# year = int(input("What is your birth year? "))
# if year > 1980 and year < 1995:         #If we give year<1994 here, Wen we input 1994 in o/p, It simply exit without printing the print Statement.
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

#4.Fix the errors
# age = int(input("How old are you? "))  #if we miss int here, it shows error because it cant compare a string and a integer value
# if age > 18:
#     print(f"You can drive at age {age}")   #we should specify 'f' string here, To age must be visible in output

#5.Print is your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Enter the pages ina book: "))       #Be careful in using of ==(assignment operator)
# word_per_page = int(input("Enter words per page: "))
# total=pages*word_per_page
# print(total)

#6.Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)   #Be careful of your indendation
#     print(b_list)
# mutate([1,2,3,5,8,13])
