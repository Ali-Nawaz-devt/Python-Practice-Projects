#Guess the number 
import random
number=random.randint(1,30)
print(number)
print("WellCome to Guess the number Game")
print("----------------------------------")
print("Enter  the number (1,30) : ")
Guesses=0
while True:
     guess=int (input())
     if guess==number :
          Guesses+=1
          print(f'Congrats you Found the in {Guesses} Attempts')
          break
     elif guess<number:
          print("Too low")
          Guesses+=1
     elif guess>number and guess<=30:
          print('Too high')
          Guesses+=1
     else:
          print("You exceed the Range ")
          Guesses+=1
     print("Guess Again : ")
     


  