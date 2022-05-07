import random

class Game:

    #Initializes three instance attributes for the object
    def __init__(self, word, lives):
        self.word = word
        self.lives = lives
        self.guessedLetters = []

    #Returns the number of remaining lives
    def get_lives(self):
        return self.lives

    #Removes a single life from the current amount
    def remove_lives(self):
        self.lives = self.lives - 1

    #Returns a list containing all of the guessed letters
    def get_guessed_letters(self):
        self.guessedLetters.sort()
        return self.guessedLetters

    #Adds a user's guessed letter to the list
    def add_guessed_letters(self, letter):
        self.guessedLetters.append(letter)

    #This displays the blanks or guessed letters for the word
    def display_blanks(self):
        blanks = ''
        for i in self.word:
            if i in self.guessedLetters:
                blanks = blanks + i + ' '
            else:
                blanks = blanks + '_ '
        print(blanks)

    #This checks if the input letter is contaiend in the word
    def check(self, letter):
        if letter in self.word:
            return True
        return False

    #This checks if the user won by guessing all the letters in the word
    def won(self):
        count = 0
        for i in self.word:
            if i in self.guessedLetters:
                count = count + 1
        return count == len(self.word)



def get_word():
    word_list = ['business', 'reviews', 'shipping', 'december', 'provided', 'programs']
    return word_list[random.randint(0,len(word_list))] 


def start():
    
    word = get_word()
    lives = 6
    game = Game(word,lives)

    while True:
        game.display_blanks()
 
        guess = str(input('Please enter a letter: ')).lower()
        game.add_guessed_letters(guess)
        if not game.check(guess):
            game.remove_lives()
        print("Guessed letters :" + str(game.get_guessed_letters()))
    
        if game.get_lives()==0:
            print("Sorry, you did not win the game, the word was: " + game.word)
            break
    
        elif game.won():
            game.display_blanks()
            print("Congrats, you've won the game and guessed the word: " + game.word)
            break
        print("Lives remaining: "+ str(game.get_lives()))
start()   
