#Function with outputs
# def format_name(f_name,l_name):
#     formated_f_name = f_name.title()           #.title is used to write the words in correct manner i.e only first letter is caps later all letters will be small
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# print(format_name("MaNoHAr","RAO"))

#More on return keyword
# def format_name(f_name,l_name):
#     formated_f_name = f_name.title()          
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# print(format_name(input("What is ur first name? "),
#                   input("What is ur last name? ")))

# If we doesnt provide any names in the o/p it will print the return statement.... 
# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide the valid inputs"      
#     formated_f_name = f_name.title()          
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# print(format_name(input("What is ur first name? "),
#                   input("What is ur last name? ")))

####### Docstrings   """  """       # It can also used as comment lines 
# def format_name(f_name,l_name):
#     """Take a first and last name and format it 
#     to return the title case version of the name"""
#     if f_name == "" or l_name == "":
#         return "You didn't provide the valid inputs"      
#     formated_f_name = f_name.title()          
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
# print(format_name)
# print(format_name(input("What is ur first name? "),
#                   input("What is ur last name? ")))


##############The working CALCULATOR#############


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():

  num1 = float(input("Enter the number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()