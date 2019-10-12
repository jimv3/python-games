import random
import time


def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
        return 1
    else:
        print('Gobbles you down in one bite!')
        return 0


playAgain = 'yes'
gamesPlayed = 0
gotTreasure = 0
while playAgain == 'yes' or playAgain == 'y':
    gamesPlayed += 1
    displayIntro()
    caveNumber = chooseCave()
    gotTreasure += checkCave(caveNumber)

    playAgain = ''
    while not playAgain:
        print('Do you want to play again? ([y]es, [n]o or [s]tatistics)')
        playAgain = input()
        if playAgain == 'statistics' or playAgain == 's':
            print(f'You have played {gamesPlayed} games.')
            print(f'You have gotten treasure {gotTreasure} times and have been eaten {gamesPlayed - gotTreasure} times.')
            print(f'You have gotten treasure {gotTreasure / gamesPlayed * 100:.2f}% of the time.')
            playAgain = ''
