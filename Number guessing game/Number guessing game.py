from art import logo
import random
print(logo)
print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100.")
difficulty = input("choose a Difficulty. Type 'easy' or 'hard': ")



def game():
  attempts = 0
  guess = int(input("make a guess: "))
  n = random.randint(1,100)
 # print(n, 'is computers number') #cheating
  
  if n > guess:
    print("Too low")
    
  elif n < guess:
    print("Too low")
    
  elif n == guess:
    print(f"You got it ! , the ansewer was {n}.")

if difficulty == "easy":
  attempts =10
  print(f"You have {attempts} attempts remaining to guess the number.")
  while attempts >0:
    game()
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
  
elif difficulty == "hard" :
  attempts =5
  print(f"You have {attempts} attempts remaining to guess the number.")
  while attempts >0:
    game()
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")

