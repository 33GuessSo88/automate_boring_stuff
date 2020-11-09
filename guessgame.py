import random

secret_number = random.randint(1, 20)
guess = ""
no_of_guesses = 1

print('Let us play a guessing game')
print('Guess a number between 0 and 20')
print(secret_number)
guess = int(input())
while guess != secret_number:
    if guess < secret_number:
        print('Your guess is too low')
        print('Take another guess')
        guess = int(input())
        no_of_guesses = no_of_guesses + 1
    elif guess > secret_number:
        print('Your number is too high')
        print('Take another guess')
        guess = int(input())
        no_of_guesses = no_of_guesses + 1
    else:
        break
if guess == secret_number:
    print('yes!')

'''
This is how the book solved it
# This is a guess the number game.
 import random
 secretNumber = random.randint(1, 20)
 print('I am thinking of a number between 1 and 20.')
 # Ask the player to guess 6 times.
 for guessesTaken in range(1, 7):
 print('Take a guess.')
 guess = int(input())
 if guess < secretNumber:
 print('Your guess is too low.')
 elif guess > secretNumber:
 print('Your guess is too high.')
 else:
 break # This condition is the correct guess!
 if guess == secretNumber:
 print('Good job! You guessed my number in ' + str(guessesTaken) + '
 guesses!')
 else:
 print('Nope. The number I was thinking of was ' + str(secretNumber))
'''