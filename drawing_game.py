import random
import time

words = ['Light', 'Ocean', 'Fruit Tree', 'Sunflowers', 'Sun', 'Moon',
         'Stars', 'Robin (bird)', 'Shark', 'Man', 'Woman', 'Giraffe', 'Elephant']

scores = [0, 0]

while len(words):
    word = random.choice(words)
    words.remove(word)
    print(f'The word is: {word}')
    print()
    team = -1
    while team < 1 or team > 2:
        print('Which team guessed correctly (1 or 2)? ', end='')
        try:
            team = int(input())
        except ValueError:
            print('Please only enter the number 1 or the number 2')

    scores[team - 1] += 1
print(f'Team {scores.index(max(scores)) + 1} wins!!')