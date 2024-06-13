#Namespaces : Local vs Global Scope 

#Local Scope : Exits within function(inside only)
# def drink():
#     water="2-lt"
#     print(water)
# drink()

#Global Scope 
# player_health=10
# def drink():
#     water="2-lt"
#     print(player_health)     #valid ouside the function also because it is declared globally
# drink()
# print(player_health)

# There is no Block Scope in Python means we shud declare and print variables only inside ,,,, No access to global variables inside function 

#Modifying Global Scope
enemies=1
def inc_enemies():
    global enemies      #without this declaration we will get error, be careful while using global
    enemies+=1
    print(f"Enemies inside function: {enemies}")
inc_enemies()
print(f"Enemies outside function: {enemies}")

#using return can make changes 
# enemies=1
# def inc_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1
# enemies = inc_enemies()
# print(f"Enemies outside function: {enemies}")

#Global constants
# PI = 3.14159  #shud define using uppercase to remember it is a Global Constant and never be changed again.
#URL = "hcvs_jbskjb"

######## GUESS THE NUMBER GAME,,,,,,,,......

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
