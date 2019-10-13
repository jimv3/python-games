# This is a Guess the Number game.
import random

MAX_GUESSES = 6
guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print(f'Well, {myName}, I am thinking of a number between 1 and 20. See if you can get it in {MAX_GUESSES} or fewer guesses.')

for guessesTaken in range(MAX_GUESSES):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = guessesTaken + 1
    print(
        f'Good job, {myName}! You guessed my number in {guessesTaken} guesses!')
if guess != number:
    print(f'Nope. The number I was thinking of was {number}.')
