import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

words = {}
words['animal'] = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck ' +
         'eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt ' +
         'otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep ' +
         'skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra').split()
words['city'] = ('amsterdam asheville athens atlanta birminham chattanooga huntsville knoxville memphis nashville ' +
         'tallahassee topeka chicago denver boulder flagstaff missoula detroit indianapolis boston tampa miami orlando ' +
         'omaha seattle portland murfreesboro shelbyville smyrna lavergne hendersonville gallatin lebanon watertown ' +
         'gainsville jacksonville hershey pittsburgh lewisburg cornersville bucksnort columbia cincinnati').split()
words['color'] = ('blue brown amber orange red yellow green purple indigo cyan magenta black white lavender mauve ' + 
         'lilac tan beige teal pink gray').split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord, category):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    print(category.upper())
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')

    print()


def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
category = random.choice(list(words.keys()))
secretWord = getRandomWord(words[category])
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord, category)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print(f'Yes! The secret word is {secretWord}! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord, category)
            print(
                f'You have run out of guesses!\nAfter {len(missedLetters)} missed guesses and {len(correctLetters)} correct guesses, the word was {secretWord}.')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            category = random.choice(['animal', 'city', 'color'])
            secretWord = getRandomWord(words[category])
        else:
            break
