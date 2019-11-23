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

WORDS = {}
WORDS['animal'] = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck ' +
                   'eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt ' +
                   'otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep ' +
                   'skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra').split()
WORDS['city'] = ('amsterdam asheville athens atlanta birmingham chattanooga huntsville knoxville memphis nashville ' +
                 'tallahassee topeka chicago denver boulder flagstaff missoula detroit indianapolis boston tampa miami orlando ' +
                 'omaha seattle portland murfreesboro shelbyville smyrna lavergne hendersonville gallatin lebanon watertown ' +
                 'gainsville jacksonville hershey pittsburgh lewisburg cornersville bucksnort columbia cincinnati').split()
WORDS['color'] = ('blue brown amber orange red yellow green purple indigo cyan magenta black white lavender mauve ' +
                  'lilac tan beige teal pink gray').split()


class HangmanGame():
    def __init__(self):
        self._missed_letters = []
        self._correct_letters = []
        self._category = random.choice(list(WORDS.keys()))
        self._secret_word = self.get_random_word(WORDS[self._category])
        self._won = False

    def get_category(self):
        return self._category.upper()

    def game_is_done(self):
        foundAllLetters = True
        for i in range(len(self._secret_word)):
            if self._secret_word[i] not in self._correct_letters:
                foundAllLetters = False
                break
        self._won = foundAllLetters
        return foundAllLetters or len(self._missed_letters) == len(HANGMAN_PICS) - 1

    def make_guess(self, guessed_letter):
        if guessed_letter in self._secret_word:
            self._correct_letters.append(guessed_letter)
        else:
            self._missed_letters.append(guessed_letter)

    def missed(self):
        return self._missed_letters

    def already_guessed(self):
        return self._missed_letters + self._correct_letters

    def display_gallows(self):
        return HANGMAN_PICS[len(self._missed_letters)]

    def is_winner(self):
        return self._won

    def display_board(self):
        blanks = '_ ' * len(self._secret_word)

        for i in range(len(self._secret_word)):
            if self._secret_word[i] in self._correct_letters:
                blanks = blanks[:i*2] + self._secret_word[i] + ' ' + blanks[(i + 1) * 2:]

        return blanks

    def get_random_word(self, wordList):
        wordIndex = random.randint(0, len(wordList) - 1)
        return wordList[wordIndex]
