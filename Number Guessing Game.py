#write a program to find guesing number
import random
def number_guessing_game():
    computer = random.randrange(1,100)
    attempts = 0
    while True:
        user = int(input("Guess a number from range(1-100):"))
        
        attempts+=1
        if computer==user:
            print(f"🎉 Your guess is correct! The number was {computer}.")
            print(f"You guessed it in {attempts} attempts.")
            break
            
        elif computer<user:
            print("Too Low! Try Again!")
        else:
            print("Too High! Try Again!")
            
        if attempts==50:
            print("Sorry! You've reached the maximum attempts (50).")
            print(f"The number was {computer}.")
            break


number_guessing_game()
