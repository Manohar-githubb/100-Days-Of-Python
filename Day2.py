# Data types, Numbers, Operations, Type Conversions, f-Strings and the project


# print("Hello"[0])

# char = len(input("What is ur name?"))
# nchar = str(char)
# print("Name has "+nchar+ " characters")

# a=123
# print(type(a))
# b=str(123)
# print(type(b))

# two_digit_num = input()
# first_digit = int(two_digit_num[0])
# second_digit = int(two_digit_num[1])
# two_digit_num = first_digit + second_digit
# print(two_digit_num)

# print(3*3+3/3-3)    #PEMDAS RULE : Priority goes like Parenthesis->Exponent->Multiplication->....

# height=input()
# weight=input()
# weight_as_int=int(weight)
# height_as_float=float(height)
# BMI=weight_as_int/height_as_float**2  
# print(int(BMI))

# print(round(8 / 3, 2))
# print(8 // 3)

# score=0
# height=1.5
# isWinnig=True
# print(f"your score is {score}, your height is {height}, your are winning is {isWinnig}")

# age = input()
# years=90-int(age)
# weeks=years*52
# print(f"you have {weeks} left")

# a=int("5")/int(2.7)
# print(type(a))


#Project Number 2 : Tip Calculator
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10,12,or 15? "))
# people = int(input("How many peole would split the bill? "))
# bill_with_tip = tip/100*bill + bill
# bill_per_person = bill_with_tip / people
# final_amount = round(bill_per_person,2)
# final_amount = "{:.2f}".format(bill_per_person) # This statement will help when your final answer is of 33.6 and it gives the result 33.60 
# print(f"Each person should pay: ${final_amount}")